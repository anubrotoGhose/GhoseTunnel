from nsescraper.nsetools.nsetools.nse import Nse
from fastapi import FastAPI
import asyncio

nse = Nse()
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id
    }



async def company_data(company_ticker):
    return await asyncio.to_thread(nse.get_quote, company_ticker)

@app.get("/company_quote/{company_ticker}")
async def company_profile(company_ticker: str):
    profile_data = await company_data(company_ticker)
    return {
        company_ticker: profile_data
    }