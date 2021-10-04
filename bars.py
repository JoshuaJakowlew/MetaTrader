import MetaTrader5 as mt5
import pandas as pd
import json

class Rates:
  def __init__(self):
    if not mt5.initialize():
      raise RuntimeError(f"initialize() failed, error code = {mt5.last_error()}")
  
  def __del__(self):
    mt5.shutdown()

  def copy_from(self, utc_from, count, pair, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_from(pair, timeframe, utc_from, count)
    return self.__serialize(pd.DataFrame(rates))

  def copy_from_pos(self, count, pair, start_pos=0, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_from_pos(pair, timeframe, start_pos, count)
    return self.__serialize(pd.DataFrame(rates))

  def copy_rates_range(self, date_from, date_to, pair, timeframe=mt5.TIMEFRAME_M1):
    rates = mt5.copy_rates_range(pair, timeframe, date_from, date_to)
    return self.__serialize(pd.DataFrame(rates))

  def __serialize(self, dataframe):
    dataframe = dataframe.to_json(orient="records")
    dataframe = json.loads(dataframe) # FIXME: unnecessary serialization
    return dataframe