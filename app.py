from fastapi import FastAPI
import json

# in construction to make an API endpoint for use with the scraped data
app = FastAPI()

json_file = open('data.json', 'r')
data = json.load(json_file)

#shows all phone prices
@app.get('/phoneprices/v1')
async def get_phone_prices():
  return data


#shows specific prices for apple phones
@app.get('/phoneprices/v1/apple')
async def get_apple_phone_prices():

  # will hold the keys we get from the json data where 'iphone' is present in the dictionary
  apple_phone_keys = []

  #appends the values from the apple_phone_keys via a loop to get the prices
  value_apple_holder = []
  
  # gets the names of the keys(dictionary keys that have the string iphone present in it)
  for data_items in data:
    if 'iPhone' in data_items:
      apple_phone_keys.append(data_items)
  
  # loops through the apple_phone_keys to give us an individual apple_key
  for apple_key in apple_phone_keys:
    value_apple_holder.append(data[apple_key])
  
  # makes a json data type by looping through th apple_phone_keys and looping through the value_apple_holder
  # in the format apple_phone_name(from apple_phone_keys): apple_phone_value(from value apple holder)
  dict_apple = {apple_phone_name: apple_phone_value for apple_phone_name, apple_phone_value in zip(apple_phone_keys,value_apple_holder)}

  # gives us the json data containing only apple phones and their prices
  return dict_apple




@app.get('/phoneprices/v1/samsung')
async def get_samsung_phone_prices():
  pass

@app.get('/phoneprices/v1/techno')
async def get_techno_phone_prices():
  pass


@app.get('/phoneprices/v1/oppo')
async def get_oppo_phone_prices():
  pass


