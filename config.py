import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("7699795429:AAG1DDqtYAjUkI-x79ZiPpsobgCs9eh94iQ")
ADMIN_IDS = list(map(int, os.getenv("868578453", "").split(',')))
CHANNEL_ID = os.getenv("-1001646141355")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET = os.getenv("BINANCE_SECRET")
