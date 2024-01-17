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
    # urls=["https://scontent-cdg4-1.cdninstagram.com/v/t50.2886-16/417436579_1080499526330758_215613097491880371_n.mp4?_nc_ht=scontent-cdg4-1.cdninstagram.com&_nc_cat=110&_nc_ohc=16IFgHVwS1MAX_vlAyI&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDiKh08QzohbmAmznLFYGDmOo-Ea-rI-dvtYiC2jZGR4Q&oe=65A8D3F0&_nc_sid=bc0c2c196",
    # "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/10000000_1047150406337236_2744447688419754220_n.mp4?efg=e30&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=104&_nc_ohc=jgweO9TBii0AX805z1F&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCy0Rx7pPDeSKkaWQjMkzSU4pFBS3HROm3SRmY_R-JY8Q&oe=65AAF1BF&_nc_sid=bc0c2c26764",
    # "https://scontent-cdg4-2.cdninstagram.com/v/t66.30100-16/319808562_2258517181013545_1850716767111014688_n.mp4?_nc_ht=scontent-cdg4-2.cdninstagram.com&_nc_cat=101&_nc_ohc=ZH19G6R1_RsAX_tqJqx&edm=APU89FABAAAA&ccb=7-5&oh=00_AfCj7f11R1xPcHSpFq8s9A9h6oRZMnSKEFvWj4y8ljFDfQ&oe=65A88DE7&_nc_sid=bc0c2c12411",
    # "https://scontent-cdg4-3.cdninstagram.com/v/t66.30100-16/44594778_285924937463706_4571124146553048690_n.mp4?efg=e30&_nc_ht=scontent-cdg4-3.cdninstagram.com&_nc_cat=106&_nc_ohc=q4lVGWdEklkAX9kAXf0&edm=APU89FABAAAA&ccb=7-5&oh=00_AfDVbYMTQuW7WQx1opYYXP8MksXc9AYEQVSkeFdaxqx92w&oe=65AC1C4B&_nc_sid=bc0c2c4431"
    # ]
    # response = requests.get(urls[int(index)])
    # with open("temp/video.mp4", "wb") as file:
    #     file.write(response.content)
    # return FileResponse("temp/video.mp4")
    return FileResponse("temp/old_video.mp4")