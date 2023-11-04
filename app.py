from fastapi import FastAPI
import json

# in construction to make an API endpoint for use with the scraped data
app = FastAPI()

@app.get('/phoneprices/v1')
async def get_phone_prices():
  json_file = open('data.json', 'r')
  data = json.load(json_file)
  return data