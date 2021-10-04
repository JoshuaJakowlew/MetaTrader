from datetime import datetime
import MetaTrader5 as mt5
 
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
# import pytz module for working with time zone
import pytz
 
class Rates:
  def __init__(self):
    if not mt5.initialize():
      raise RuntimeError(f"initialize() failed, error code = {mt5.last_error()}")
  
  def close(self):
    mt5.shutdown()

  def copy_from(self, utc_from, count, pair, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_from(pair, timeframe, utc_from, count)
    return pd.DataFrame(rates)

  def copy_from_pos(self, count, pair, start_pos=0, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_from_pos(pair, timeframe, start_pos, count)
    return pd.DataFrame(rates)

  def copy_rates_range(self, date_from, date_to, pair, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_range(pair, timeframe, date_from, date_to)
    return pd.DataFrame(rates)

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2021, 1, 10, tzinfo=timezone)


# rates = Rates()
# data = rates.copy_from(utc_from, 10, "EURUSD")
# print(data)


# result = data.to_json(orient="records")
# print(result)