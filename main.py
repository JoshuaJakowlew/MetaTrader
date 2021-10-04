from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import json

from datetime import datetime
import pytz

import MetaTrader5 as mt

import bars
from bars import Rates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

rates = Rates()


@app.get("/updates/init")
async def updates_init(count: int = 10):
  data = rates.copy_from_pos(count, "EURUSD")
  return data

@app.get("/updates")
async def updates(date_from: float):
  date_from = datetime.fromtimestamp(date_from)
  date_to = datetime.now()
  data = rates.copy_rates_range(date_from, date_to, "EURUSD")
  return data