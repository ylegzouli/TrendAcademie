#%%
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from ranking import mock_products, mock_brands
import requests
from product import get_product_id, get_product_image, get_product_name, get_product_brand, get_product_description, get_influencer, process_news
from ranking import news_to_product_occurence, get_cumulative_likes, get_cumulative_comments
import pickle

news_all = pickle.load(open("data/news_data.pkl", "rb"))[0]

news_month, news_week, news_day = process_news(news_all)


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def get_products():
    return mock_products()

@app.get("/brands")
def get_brands():
    return mock_brands()


@app.get("/videos/{index}")
def get_video(index):
    urls=[
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/10000000_1810461859469680_7186422982601872063_n.mp4?_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=104&_nc_ohc=XKtTHsCOSZEAX_v0hnj&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCBg6DZRoSdVucUXpBieZ073uXL3ZLBW45bHtF7sSE8CA&oe=65AA6B2F&_nc_sid=bc0c2c",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/10000000_865624752232828_420909119339530190_n.mp4?_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=104&_nc_ohc=S7OlkE0ZF2cAX9UjXgI&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCfChBT3JuIaUiAoYFwWdUIVVk8qQ1vigDscVcChwnXvA&oe=65A9CCC4&_nc_sid=bc0c2c",
        "https://scontent-cdg4-1.cdninstagram.com/v/t50.2886-16/417436579_1080499526330758_215613097491880371_n.mp4?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=110&_nc_ohc=16IFgHVwS1MAX8eqTmD&edm=APU89FABAAAA&ccb=7-5&oh=00_AfC7bWvuHQFfzQLXSbs2em7A7V6zImhYPJetaU62G4wdkg&oe=65AA2570&_nc_sid=bc0c2c",
        "https://scontent-cdg4-1.cdninstagram.com/v/t50.2886-16/10000000_212147611977710_627073631995185810_n.mp4?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=102&_nc_ohc=ievxXfm7KaAAX84H80b&edm=APU89FABAAAA&ccb=7-5&oh=00_AfAIC_3muZH7S2GTu3AYuKRBLxpygVDg-fxbZDenOL-aNA&oe=65AA1F21&_nc_sid=bc0c2c",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/320273308_1307870979832547_1157995225234008483_n.mp4?_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=111&_nc_ohc=Jg0ePAl-HrwAX-Lf-fl&edm=APU89FABAAAA&ccb=7-5&oh=00_AfBNPVbfAGsDYDM6PCngivfSUlJL3dEnpLa65a-ob3NcfA&oe=65AA03C8&_nc_sid=bc0c2c",
        "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/334658098_923339552051244_7629673561791266244_n.mp4?efg=e30&_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=100&_nc_ohc=I2GvTqhxgskAX-wi23m&edm=APU89FABAAAA&ccb=7-5&oh=00_AfBJOMhTbxHRvcc4qQbBX5X0MQkuxhR1z4y7Qo29hAf_Nw&oe=65ACDFD0&_nc_sid=bc0c2c",
        "https://scontent-cdg4-1.cdninstagram.com/v/t66.30100-16/120692422_2064749973904796_8359243380075642979_n.mp4?efg=e30&_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=108&_nc_ohc=j60M2quJpPYAX9TdmxW&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCYyltOUOV_KRTSjEU9tmEYrcXPTw1n5QS3CjYXkMHY3Q&oe=65ADD74E&_nc_sid=bc0c2c",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/121441441_1449427122643924_792112154193955508_n.mp4?_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=104&_nc_ohc=TMRNyja9iBUAX_uHz5R&edm=APU89FABAAAA&ccb=7-5&oh=00_AfA0_98MsfkQ46gmXiddeNRAwk4mjjdGritJ9Wb9Xyg_8g&oe=65AA3F4A&_nc_sid=bc0c2c",
    ]
    response = requests.get(urls[int(index)])
    with open("frontend/tiktok-clone/src/temp/old_video.mp4", "wb") as file:
        file.write(response.content)
    return FileResponse("frontend/tiktok-clone/src/temp/old_video.mp4")


#%%
@app.get("/home/{time}")
def get_home_data(time):
    if time == "month":
        news = news_month
    elif time == "week":
        news = news_week
    elif time == "day":
        news = news_day

    df = news_to_product_occurence(news)
    product_names = df['product_name'].tolist()
    
    products = []
    for name in product_names:
        product_id = get_product_id(name)  # Assuming get_id(name) returns the product id
        product_image = get_product_image(name)  # Assuming get_image(name) returns the image URL
        product_likes = get_cumulative_likes(name, news) / 1000
        product_brand = get_product_brand(product_id)
        try:
            product_mention = df[df['product_name'] == name]["occurrences"].values[0]
        except:
            product_mention = 0
        
        product = {
                "product_id": str(product_id),
                "product_name": name,
                "product_image": product_image,
                "product_mentions": str(product_mention*4),
                "product_likes": str(product_likes),
                "product_brand": product_brand,
            }
        products.append(product)

    return {
        "products": products,
        "brands": [],
    }

@app.get("/product/{time}/{product_id}")
def get_product(time, product_id):
    if time == "month":
        news = news_month
    elif time == "week":
        news = news_week
    elif time == "day":
        news = news_day
    product_id = int(product_id)
    product_name = get_product_name(product_id)
    product_image = get_product_image(product_name)
    product_brand = get_product_brand(product_id)
    product_description = get_product_description(product_id)
    product_likes = get_cumulative_likes(product_name, news) / 1000
    product_comment = get_cumulative_comments(product_name, news) / 1000
    product_influencer = get_influencer(product_id, news)
    try:
        product_mentions = news_to_product_occurence(news)[news_to_product_occurence(news)['product_name'] == product_name]["occurrences"].values[0] * 4
    except:
        product_mentions = 0
    return {
        "id": str(product_id),
        "name": product_name,
        "image": product_image,
        "brand": product_brand,
        "description": product_description,
        "likes": str(product_likes),
        "mentions": str(product_mentions),
        "comment": str(product_comment),

        "in_stock": "In stock",
        "influencer": product_influencer,
        "similar": "",
        "compatible": "",
        "category": "",
        "highlight": "",
    }

# %%