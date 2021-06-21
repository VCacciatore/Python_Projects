import requests
import pandas as pd
import json

urls = ['https://www.harney.com/collections/black-tea/products.json',
        'https://ahmadteausa.com/collections/popular/products.json',
        'https://tea-tao.com/collections/loose-tea-in-pouch/products.json']

tea_list = []

for url in urls:

    r = requests.get(url)

    data = r.json()

    

    for item in data['products']:
        name = (item['title'])
        for variant in item['variants']:
            price = variant['price']
            size = variant['grams']
        
            tea = {
                'name': name,
                'price': price,
                'size in grams': size,
            }
        
            tea_list.append(tea)

    #print(tea_list)

df = pd.DataFrame(tea_list)

df.to_csv('tea_drinks_and_prices.csv')
print('csv created')