import requests
import pandas as pd

url = "https://api.finmindtrade.com/api/v4/data"
parameter = {
    "dataset": "TaiwanStockPrice",
    "data_id": "2330",
    "start_date": "2022-06-13",
    "end_date": "2022-06-24"
}
r = requests.get(url, params=parameter)
data = r.json()
stock_deal_info = data["data"]
print(pd.DataFrame(stock_deal_info))

