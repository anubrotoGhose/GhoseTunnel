# NSE Stock Data API

This Flask-based project provides various endpoints to fetch real-time stock data from the National Stock Exchange (NSE) using the `nsetools` library.

## Features
- Fetch all stock codes
- Validate stock ticker codes
- Retrieve company quotes
- Fetch 52-week high and low stock prices
- Retrieve index lists and index quotes
- Get top gainers and losers in specific indices
- Fetch advances and declines for a company
- Retrieve stocks in a specific index
- Get future quotes for stocks

## Installation

### Prerequisites
Ensure you have Python 3.10+ installed.

### Clone the Repository
```sh
git clone <repository-url>
cd <project-folder>
```

### Create and Activate a Virtual Environment
```sh
python -m venv tempvenv
source tempvenv/bin/activate  # On macOS/Linux
# OR
tempvenv\Scripts\activate    # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Run the API Server
```sh
python main.py
```

### Available Endpoints

#### Base URL: `http://localhost:5000`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns a welcome message |
| `/items/<item_id>` | GET | Returns an item with the given ID |
| `/get_all_stock_codes` | GET | Returns all stock codes traded on NSE |
| `/is_valid_code/<code>` | GET | Checks if the given company ticker is valid |
| `/get_company_quote/<code>` | GET | Fetches and returns a company quote for the given code |
| `/get_52_week_high/<code>` | GET | Returns the 52-week high for a given stock |
| `/get_52_week_low/<code>` | GET | Returns the 52-week low for a given stock |
| `/get_index_list` | GET | Returns a list of all available indices |
| `/get_all_index_quote` | GET | Fetches and returns all index quotes |
| `/get_top_gainers` | GET | Fetches the top gainers in NIFTY |
| `/get_top_gainers/<index>` | GET | Fetches the top gainers in a specified index |
| `/get_top_losers` | GET | Fetches the top losers in NIFTY |
| `/get_top_losers/<index>` | GET | Fetches the top losers in a specified index |
| `/get_advances_declines/<code>` | GET | Fetches advances/declines for a given company |
| `/get_stocks_in_index/<index>` | GET | Returns all stocks in a specified index |
| `/get_top_gainers_losers/<direction>/<index>` | GET | Fetches top gainers or losers based on direction (up/down) |
| `/get_future_quote/<code>/<expiry_date>` | GET | Fetches future quotes for a given stock and expiry date |

## Notes
- Ensure that `nsetools` is installed and correctly configured.
- Replace `<repository-url>` with the actual GitHub repository URL.
- If `nsetools` fails to work, consider using `nsepython` as an alternative.

## License
MIT License

## Author
Anubroto Ghose