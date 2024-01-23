# %%
import requests
    
link_similar = 'https://sephora.cnstrc.com/recommendations/v1/pods/similar-products-test?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=5&item_id=P01018539'
link_complementaire = "https://sephora.cnstrc.com/recommendations/v1/pods/pdp-frequently-bought-together?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=3&item_id=P01018539"

link_similar_2 = "https://sephora.cnstrc.com/recommendations/v1/pods/similar-products-test?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=15&num_results=5&item_id=P461148"
link_complementaire_2 = "https://sephora.cnstrc.com/recommendations/v1/pods/pdp-frequently-bought-together?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=15&num_results=3&item_id=P461148"

api_key="https://distillery.pixlee.co/api/v2/albums/66731130/photos?api_key=LKDci0fIQ7BCr9VKL9e0&region_id=2784&sku=2389542&page=1&per_page=30"

response = requests.get(link_similar)

#%%

print(response.status_code)
print(response.text)
import json

with open('data/test.json', 'w') as file:
    file.write(response.text)
# %%
    

    
