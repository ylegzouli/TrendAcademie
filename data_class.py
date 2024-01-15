from pydantic import BaseModel
from datetime import datetime
from typing import List

class News(BaseModel):
    title: str
    url: str
    source_type: str
    content: str

    
    publishedAt: datetime

    product_list: List[str] = []
    brand_list: List[str] = []