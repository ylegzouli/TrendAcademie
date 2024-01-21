#%%

import csv
from newspaper import Article

print("get urls")

# Step 1: Read URLs from the CSV file
urls = []
with open('data/urls.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        urls.append(row['URL'])

#%%
# import requests
# import json
# from newspaper import Article




# for url in urls:
#     print('---------------------------------------------')
#     print(idx)
#     print(title)
#     article = Article(url)
#     article.download()
#     article.parse()
#     title = article.title.split(' - ')[0]
#     idx = url.split('-')[-1]
#     url_similar = f"https://sephora.cnstrc.com/recommendations/v1/pods/similar-products-test?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=5&item_id={idx}"
#     response_similar = requests.get(url_similar)
#     similar = json.loads(response_similar.text)
#     print("\nSIMILAR PRODUCTS")
#     for i in range(len(similar['response']['results'])):
#         print(similar['response']['results'][0]['value'].split(' - ')[0])
#         print(similar['response']['results'][0]['data']['brandName'])
#         print(similar['response']['results'][0]['data']['image_url'])



#     url_complementaire = f"https://sephora.cnstrc.com/recommendations/v1/pods/pdp-frequently-bought-together?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=5&item_id={idx}"
#     response_complementaire = requests.get(url_complementaire)
#     complementaire = json.loads(response_complementaire.text)
#     print("\nCOMPLEMENTAIRE PRODUCTS")
#     for i in range(len(complementaire['response']['results'])):
#         print(complementaire['response']['results'][0]['value'].split(' - ')[0])
#         print(complementaire['response']['results'][0]['data']['brandName'])
#         print(complementaire['response']['results'][0]['data']['image_url'])
    

#%%
import pandas as pd  
DATA = pd.read_csv('data/sephora.csv')

import requests
import json

data = {}

for url in urls:
    try:
        print('---------------------------------------------')
        idx = url.split('-')[-1]
        article = Article(url)
        article.download()
        article.parse()
        title = article.title.split(' - ')[0]
        print(title)
        print(idx)

        # Similar Products
        url_similar = f"https://sephora.cnstrc.com/recommendations/v1/pods/similar-products-test?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=5&item_id={idx}"
        response_similar = requests.get(url_similar)
        similar = json.loads(response_similar.text)
        similar_products = []
        for product in similar['response']['results']:
            
            similar_products.append({
                "name": product['value'].split(' - ')[0],
                "brand": product['data']['brandName'],
                "image_url": product['data']['image_url']
            })
            print(similar_products[-1]['name'])

        # Complementary Products
        url_complementaire = f"https://sephora.cnstrc.com/recommendations/v1/pods/pdp-frequently-bought-together?c=ciojs-client-2.41.0&key=u7PNVQx-prod-en-us&i=f47eb19c-7d6a-45b9-9124-7f85d8e3d690&s=17&num_results=5&item_id={idx}"
        response_complementaire = requests.get(url_complementaire)
        complementaire = json.loads(response_complementaire.text)
        complementary_products = []
        for product in complementaire['response']['results']:
            complementary_products.append({
                "name": product['value'].split(' - ')[0],
                "brand": product['data']['brandName'],
                "image_url": product['data']['image_url']
            })
            print(complementary_products[-1]['name'])

        # Add to data dictionary
        data[title] = {
            "similar_products": similar_products,
            "complementary_products": complementary_products
        }
    except Exception as e:
        print(e)
        print("Error for url: ", url)
        continue


# print(data)

# Save data to JSON file
with open('data/products_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
    


# %%
