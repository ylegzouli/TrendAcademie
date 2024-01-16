from pydantic import BaseModel
# from datetime import datetime
from typing import List, Any, Optional

class News(BaseModel):
    username: str
    likes: int
    comments: int
    url: str
    source_type: str
    content: str
    
    is_video: bool
    video_url: Optional[str] = None
    video_view_count: Optional[int] = None

    
    publishedAt: Any

    product_list: List[str] = []
    brand_list: List[str] = []


# class Product( BaseModel ):
    # name: str
    # brand: str
    # url: str
    # source_type: str
    # publishedAt: Any
    # content: str
    # title: str
    # url: str
    # source_type: str
    # content: str

    
    # publishedAt: Any

    # product_list: List[str] = []
    # brand_list: List[str] = []