import pandas as pd
import mplfinance as mpf

daily = pd.read_csv(
    "examples/data/SP500_NOV2019_Hist.csv", index_col=0, parse_dates=True
)
daily.index.name = "Date"
daily.shape
daily.head(3)
daily.tail(3)

mpf.plot(daily)
