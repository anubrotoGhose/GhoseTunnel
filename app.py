# from nsescraper.nsetools.nsetools.nse import Nse
from nsetools import Nse
from fastapi import FastAPI
import asyncio
import uvicorn
nse = Nse()
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "GhoseTunnel"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id
    }

@app.get("/get_all_stock_codes")
async def nse_all_stock_codes():
    """Endpoint to fetch and return all stock codes (tickers) traded on the NSE in JSON format."""
    return await asyncio.to_thread(nse.get_stock_codes)

@app.get("/is_valid_code/{code}")
async def is_valid_ticker_checker(code: str):
    """Endpoint to fetch and return and check if company code/symbol/ticker is correct"""
    return {
        "validity": asyncio.to_thread(nse.is_valid_code, code)
    }

@app.get("/get_company_quote/{code}")
async def company_profile(code: str):
    """Endpoint to fetch and return company quote based on given code (ticker)"""
    return {
        code: await asyncio.to_thread(nse.get_quote, code)
    }

@app.get("/get_52_week_high")
async def get_52_week_high():
    """Endpoint to fetch and return get_52_week_high in JSON"""
    return await asyncio.to_thread(nse.get_52_week_high)

@app.get("/get_52_week_low")
async def get_52_week_high():
    """Endpoint to fetch and return get_52_week_low in JSON"""
    return await asyncio.to_thread(nse.get_52_week_low)

@app.get("/get_index_list")
async def get_index_list():
    """Endpoint to fetch and return index lists in JSON"""
    return await asyncio.to_thread(nse.get_index_list)

@app.get("/get_all_index_quote")
async def get_all_index_quote():
    """Endpoint to fetch and return all index_quote | json of index codes in JSON"""
    return await asyncio.to_thread(nse.get_index_list)

@app.get("/get_top_gainers")
async def get_top_gainers_default():
    """Endpoint to fetch and return top gainers in NIFTY which is default in JSON"""
    return await asyncio.to_thread(nse.get_top_gainers, "NIFTY")

@app.get("/get_top_gainers/{index}")
async def get_top_gainers(index: str):
    """Endpoint to fetch and return top gainers based on index in JSON"""
    return await asyncio.to_thread(nse.get_top_gainers, index)

@app.get("/get_top_losers")
async def get_top_losers_default():
    """Endpoint to fetch and return top losers in nifty which is default in JSON"""
    return await asyncio.to_thread(nse.get_top_losers, "NIFTY")

@app.get("/get_top_losers/{index}")
async def get_top_losers(index: str):
    """Endpoint to fetch and return top losers based on index in JSON"""
    return await asyncio.to_thread(nse.get_top_losers, index)

@app.get("/get_advances_declines/{code}")
async def get_advances_declines(code: str):
    """Endpoint to fetch and return advances declines of company based on code/sympbol/ticker in JSON"""
    return await asyncio.to_thread(nse.get_advances_declines, code)

@app.get("/get_stocks_in_index/{index}")
async def get_stocks_in_index(index: str):
    """Endpoint to fetch and return stocks in index in JSON"""
    return await asyncio.to_thread(nse.get_stocks_in_index, index)

@app.get("/get_top_gainers_losers/{direction}/{index}")
async def get_advances_declines(direction: str, index: str):
    """Endpoint to fetch and return top gainers/losers based on direction and index in JSON"""
    return await asyncio.to_thread(nse._get_top_gainers_losers, direction, index)

@app.get("/get_future_quote/{code}/{expiry_date}")
async def get_future_quote(code: str, expiry_date: str):
    """Endpoint to fetch and return future quote based on code (ticker) in JSON"""
    return await asyncio.to_thread(nse.get_future_quote, code, expiry_date)

# if __name__ == "__main__":
#     uvicorn.run("main:app", port=5000, log_level="info")