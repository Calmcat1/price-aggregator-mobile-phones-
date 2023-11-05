from fastapi import FastAPI
import json

# in construction to make an API endpoint for use with the scraped data
app = FastAPI()

json_file = open('../data.json', 'r')
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



# for samsung, comments similar to the apple one above, just replace apple with samsung :>
@app.get('/phoneprices/v1/samsung')
async def get_samsung_phone_prices():
 
  samsung_phone_keys = []
  value_samsung_holder = []
  
 
  for data_items in data:
    if 'sung' in data_items:
      samsung_phone_keys.append(data_items)
  
 
  for samsung_key in samsung_phone_keys:
    value_samsung_holder.append(data[samsung_key])
 
  dict_samsung = {samsung_phone_name: samsung_phone_value for samsung_phone_name, samsung_phone_value in zip(samsung_phone_keys,value_samsung_holder)}


  return dict_samsung

# for Tecno, comments similar to the apple one above, just replace apple with Tecno :>
@app.get('/phoneprices/v1/Tecno')
async def get_techno_phone_prices():
    Tecno_phone_keys = []
    value_Tecno_holder = []
    
   
    for data_items in data:
      if 'Tecno' in data_items:
        Tecno_phone_keys.append(data_items)
    
   
    for Tecno_key in Tecno_phone_keys:
      value_Tecno_holder.append(data[Tecno_key])
   
    dict_Tecno = {Tecno_phone_name: Tecno_phone_value for Tecno_phone_name, Tecno_phone_value in zip(Tecno_phone_keys,value_Tecno_holder)}

  
    return dict_Tecno


# for Oppo, comments similar to the apple one above, just replace apple with Oppo :>
@app.get('/phoneprices/v1/Oppo')
async def get_oppo_phone_prices():
  Oppo_phone_keys = []
  value_Oppo_holder = []
  
 
  for data_items in data:
    if 'Oppo' in data_items:
      Oppo_phone_keys.append(data_items)
  
 
  for Oppo_key in Oppo_phone_keys:
    value_Oppo_holder.append(data[Oppo_key])
 
  dict_Oppo = {Oppo_phone_name: Oppo_phone_value for Oppo_phone_name,Oppo_phone_value in zip(Oppo_phone_keys,value_Oppo_holder)}

  return dict_Oppo


