from pydantic import BaseModel
# from datetime import datetime
from typing import List, Any

class News(BaseModel):
    title: str
    url: str
    source_type: str
    content: str

    
    publishedAt: Any

    product_list: List[str] = []
    brand_list: List[str] = []