from cProfile import label
from locale import currency
from click import style
import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt
crypto = "BTC"
currency = "USD"
start = dt.datetime(2021, 10, 3)
end = dt.datetime.now()
btc = web.DataReader(f"{crypto}-{currency}", "yahoo",start,end)
eth = web.DataReader(f"ETH-{currency}", "yahoo",start,end)

# plt.yscale("log")
# print(data)
plt.plot(btc["close"], label ="BTC")
plt.plot(eth["close"], label ="ETH")
plt.legend(loc="upper left")
plt.show()
# plt.plot(data["Close"])
# plt.show()
# mpf.plot(data, type="candle", style="yahoo", title=f"{crypto} Price")
# mpf.plot(btc,type="candle", style="yahoo", volume=True)