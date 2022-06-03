import unicorn_binance_websocket_api
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///LivepriceDB.db")

symbols = ["btcusdt", "ethusdt", "bnbusdt", "xrpusdt", "solusdt", "adausdt"]

ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(["kline_1m"], symbols, output="UnicornFry")


def SQLImport(data):
    klines = data["kline"]
    frame = pd.DataFrame([klines])
    frame.close_price = frame.close_price.astype(float)
    if data["kline"]["is_closed"]:
        frame.to_sql(frame.symbol[0], engine, index=False, if_exists="append")


while True:
    data = ubwa.pop_stream_data_from_stream_buffer()
    if data:
        if len(data) > 3:
            # SQLimport0HLC(data)
            SQLImport(data)
