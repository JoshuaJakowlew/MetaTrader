from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse, Response
from fastapi.templating import Jinja2Templates

import json

from datetime import datetime
import MetaTrader5 as mt

from bars import Rates

from pathlib import Path

app = FastAPI()
rates = Rates()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
	return templates.TemplateResponse("chart.html", {"request": request})

@app.get("/js/{name}")
async def get_js(name: str):
  file_path = f"js/{name}"
  return FileResponse(file_path, media_type="text/javascript")

@app.get("/updates/init")
async def updates_init(count: int = 10):
  data = rates.copy_from_pos(count, "EURUSD")
  return data

@app.get("/updates/get")
async def updates(date_from: float, drop_first=False):
  date_from = datetime.fromtimestamp(date_from + int(drop_first))
  date_to = datetime.now()
  data = rates.copy_rates_range(date_from, date_to, "EURUSD")
  return data