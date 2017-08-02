from pandas_datareader import data,wb
from datetime import datetime

df = data.DataReader("KRX:KOSPI","google")
ax = df.Close.plot()

ax.set_title("KOSPI 2016")
ax.set_ylabel("Index")
ax.set_xlim("2016-01-01","2016-11-15")