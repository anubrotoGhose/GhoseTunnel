# from nsetools import Nse

# nse = Nse()
# print(dir(nse))
from nsetools import Nse
from flask import Flask
import asyncio

nse = Nse()
app = Flask(__name__)

@app.route("/")
def home():
    return "GhoseTunnel"

@app.route("/items/<int:item_id>")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.route("/get_all_stock_codes")
async def nse_all_stock_codes():
    """Fetch and return all stock codes (tickers) traded on NSE in JSON."""
    return await asyncio.to_thread(nse.get_stock_codes)

@app.route("/is_valid_code/<code>")
async def is_valid_ticker_checker(code: str):
    """Check if the given company code/symbol/ticker is valid."""
    return {"validity": await asyncio.to_thread(nse.is_valid_code, code)}

@app.route("/get_company_quote/<code>")
async def company_profile(code: str):
    """Fetch and return company quote for a given ticker."""
    return {code: await asyncio.to_thread(nse.get_quote, code)}

@app.route("/get_52_week_high/<code>")
def get_52_week_high(code):
    """Fetch and return the 52-week high price of a given stock."""
    stock_data = nse.get_quote(code)
    if stock_data and "yearHigh" in stock_data:
        return ({"52_week_high": stock_data["yearHigh"]})
    else:
        return ({"error": "Data not available"}), 404


@app.route("/get_52_week_low/<code>")
async def get_52_week_low(code: str):
    """Fetch and return 52-week low stock prices."""
    stock_data = nse.get_quote(code)
    if stock_data and "yearLow" in stock_data:
        return ({"52_week_low": stock_data["yearLow"]})
    else:
        return ({"error": "Data not available"}), 404

@app.route("/get_index_list")
async def get_index_list():
    """Fetch and return all available NSE indices."""
    return await asyncio.to_thread(nse.get_index_list)

@app.route("/get_all_index_quote")
async def get_all_index_quote():
    """Fetch and return quotes for all indices."""
    return await asyncio.to_thread(nse.get_all_index_quote)  # Ensure this function exists

@app.route("/get_top_gainers")
async def get_top_gainers_default():
    """Fetch and return top gainers (default: NIFTY)."""
    return await asyncio.to_thread(nse.get_top_gainers, "NIFTY")

@app.route("/get_top_gainers/<index>")
async def get_top_gainers(index: str):
    """Fetch and return top gainers for a specific index."""
    return await asyncio.to_thread(nse.get_top_gainers, index)

@app.route("/get_top_losers")
async def get_top_losers_default():
    """Fetch and return top losers (default: NIFTY)."""
    return await asyncio.to_thread(nse.get_top_losers, "NIFTY")

@app.route("/get_top_losers/<index>")
async def get_top_losers(index: str):
    """Fetch and return top losers for a specific index."""
    return await asyncio.to_thread(nse.get_top_losers, index)

@app.route("/get_advances_declines/<code>")
async def get_advances_declines(code: str):
    """Fetch and return advances/declines of a company."""
    return await asyncio.to_thread(nse.get_advances_declines, code)

@app.route("/get_stocks_in_index/<index>")
async def get_stocks_in_index(index: str):
    """Fetch and return all stocks in a given index."""
    return await asyncio.to_thread(nse.get_stocks_in_index, index)

@app.route("/get_top_gainers_losers/<direction>/<index>")
async def get_top_gainers_losers(direction: str, index: str):  # Fixed duplicate function name
    """Fetch and return top gainers or losers based on direction (up/down) and index."""
    return await asyncio.to_thread(nse._get_top_gainers_losers, direction, index)

@app.route("/get_future_quote/<code>/<expiry_date>")
async def get_future_quote(code: str, expiry_date: str):
    """Fetch and return future quotes for a given stock."""
    return await asyncio.to_thread(nse.get_future_quote, code, expiry_date)

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)  # Use Flask's built-in server for development
