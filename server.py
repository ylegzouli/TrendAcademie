from fastapi import FastAPI
from fastapi.responses import FileResponse
from ranking import mock_products, mock_brands
import requests


app = FastAPI()

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

# @app.get("/get_video_info")
# def get_video_info():
#     return {
#         "video_url": "http://