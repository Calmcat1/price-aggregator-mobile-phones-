from fastapi import FastAPI
import json

# in construction to make an API endpoint for use with the scraped data
app = FastAPI()

@app.get('/phoneprices/v1')
async def get_phone_prices():
  data = json.load('data.json')
  return data