import os
import time
import pandas_datareader as web
from winotify import Notification,audio

tickers = ["AAPL","FB","NVDA","GS","WFC"]
# for ticker in tickers:
#     print(web.DataReader(ticker,"yahoo").iloc[-1]["close"])

upper_limit = [160.9,220,400,300,70]
lower_limit = [100,130,500,140,30]

while True:
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)
    time.sleep(2)
    for i in range(len(tickers)):
        if last_prices[i] > upper_limit[i]:
            toast = Notification(app_id = "Favlink stock alarm", title = "Price Alert For " + tickers[i], msg=f"{tickers[i]} Has Reached A Price Of {last_prices[i]}. You Might Want To Sell",
            # icon=os.path.join(os.join.getcwd(), "sell.png"),
            duration="long")
            toast.add_actions(label="Go to Stockbroker", launch="https://elosiubafavour.tech")    
            toast.set_audio(audio.LoopingAlarm6,loop=True)
            toast.show()
        elif last_prices[i] < lower_limit[i]:
            toast = Notification(app_id = "Favlink stock alarm", title = "Price Alert For " + tickers[i], msg=f"{tickers[i]} Has Reached A Price Of {last_prices[i]}. You Might Want To Buy",
            # icon=os.path.join(os.path.join.getcwd(), "sell.png"),
            duration="long")
            toast.add_actions(label="Go to Stockbroker", launch="https://elosiubafavour.tech")    
            toast.set_audio(audio.LoopingAlarm8,loop=True)
            toast.show()
        time.sleep(1)


