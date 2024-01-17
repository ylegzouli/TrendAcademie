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
        "https://scontent-cdg4-1.cdninstagram.com/v/t50.2886-16/417436579_1080499526330758_215613097491880371_n.mp4?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=110&_nc_ohc=16IFgHVwS1MAX_vlAyI&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDiKh08QzohbmAmznLFYGDmOo-Ea-rI-dvtYiC2jZGR4Q&oe=65A8D3F0&_nc_sid=bc0c2c196",
        "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/319808562_2258517181013545_1850716767111014688_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=101&_nc_ohc=ZH19G6R1_RsAX_tqJqx&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCj7f11R1xPcHSpFq8s9A9h6oRZMnSKEFvWj4y8ljFDfQ&oe=65A88DE7&_nc_sid=bc0c2c12411",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/44594778_285924937463706_4571124146553048690_n.mp4?efg=e30&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=106&_nc_ohc=q4lVGWdEklkAX9kAXf0&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDVbYMTQuW7WQx1opYYXP8MksXc9AYEQVSkeFdaxqx92w&oe=65AC1C4B&_nc_sid=bc0c2c4431",
        "https://scontent-cdg4-2.cdninstagram.com/v/t50.2886-16/420157391_756580589659297_9198608714297025278_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=101&_nc_ohc=f3gu2Tu7-3wAX-Z11x9&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDWBcE4tQERGh1mEZg7DMVwjMUsC9gPXaEFULfNubfKcw&oe=65A8ABCE&_nc_sid=bc0c2c4727",
        "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/319808562_2258517181013545_1850716767111014688_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=101&_nc_ohc=ZH19G6R1_RsAX_tqJqx&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCj7f11R1xPcHSpFq8s9A9h6oRZMnSKEFvWj4y8ljFDfQ&oe=65A88DE7&_nc_sid=bc0c2c12441",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/44594778_285924937463706_4571124146553048690_n.mp4?efg=e30&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=106&_nc_ohc=q4lVGWdEklkAX9kAXf0&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDVbYMTQuW7WQx1opYYXP8MksXc9AYEQVSkeFdaxqx92w&oe=65AC1C4B&_nc_sid=bc0c2c4435",
        "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/10000000_400629559005583_1793153788025731579_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=107&_nc_ohc=cgPY4BlLI5AAX--KWOl&edm=APU89FABAAAA&ccb=7-5&oh=00_AfALbFnk7jeH9F5bZGdr-5JH_WNw8vxGFyn57Dozm1hrcg&oe=65A8D0A4&_nc_sid=bc0c2c1508",
        "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/10000000_804052331483361_4024662045141313406_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=109&_nc_ohc=FrTdDEwZYZ0AX-bLWQ2&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDxxvct-rq2tvQelxg22e-06JnH0IE_ZNDgUFM5PevANA&oe=65A8A13C&_nc_sid=bc0c2c33950",
        "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/43553745_899150398568819_2128775764771834163_n.mp4?_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=111&_nc_ohc=Z51OiNschFEAX8gBQws&edm=APU89FABAAAA&ccb=7-5&oh=00_AfBwY7eKXAPqePCXb6UTCu5F-yz1s9ijOOlznVYFE7tK6g&oe=65A8BBF4&_nc_sid=bc0c2c30883"
    ]
    response = requests.get(urls[int(index)])
    with open("frontend/tiktok-clone/src/temp/old_video.mp4", "wb") as file:
        file.write(response.content)
    return FileResponse("frontend/tiktok-clone/src/temp/old_video.mp4")

# @app.get("/get_video_info")
# def get_video_info():
#     return {
#         "video_url": "http://