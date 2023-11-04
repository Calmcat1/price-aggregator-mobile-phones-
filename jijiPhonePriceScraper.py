import requests
from bs4 import BeautifulSoup
import json

#url we are scraping
url = 'https://jiji.co.ke/mobile-phones'

# aggregates all price data into this array
price_data = []
name_data = []

# holds all text concerning the price
all_prices = []
all_names = []

#for loop here used for pagination scraping using the page parameter
for i in range(1,20):
  params = {
    'page' : i
  }

  response = requests.get(url, params=params)
  soup = BeautifulSoup(response.content, 'html5lib')
  price_data.append(soup.find_all('div', 'qa-advert-price'))
  name_data.append(soup.find_all('div', 'b-advert-title-inner qa-advert-title b-advert-title-inner--div'))


# for loops, to loop through the arrays price_data and agg_price to get the text
for agg_price in price_data:
  for price in agg_price:
    all_prices.append(''.join(price.text.replace('\n', '').split()))

for agg_name in name_data:
  for name in agg_name:
    all_names.append(''.join(name.text.replace('\n', '').split()))


# creates key value pairs for json output
valuePairs = {names: prices for names, prices in zip(all_names, all_prices)}

# saves the value_pairs, dictionary in json format into a file
with open('data.json', 'w') as json_file:
  json_file.write(json.dumps(valuePairs, indent=4))


# displays data, visualizes the data
print(valuePairs)


