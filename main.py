from datetime import date, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client
import requests

STOCK = "TSLA"
COMPANY_NAME = "TeslaInc"
DATE = date.today()
YESTERDAY = DATE - timedelta(days=1)
DAY_BEFORE_YESTERDAY = DATE - timedelta(days=2)
TWO_DAYS_AGO = DATE - timedelta(days=3)
THREE_DAYS_AGO = DATE - timedelta(days=4)
ALPHA_VANTAGE_API = "[YOUR API]"
STOCK_URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=demo"
NEWS_API = "[YOUR API]"
NEWS_URL = "https://newsapi.org/v2/everything?q={}&apiKey={demo}"
TWILIO_ACCOUNT_SID = "[YOUR SID]"
TWILIO_AUTH_TOKEN = "[YOUR TOKEN]"
MSG = ""

stock_params = {
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API
}


def get_news(q, from_param):
    global MSG
    newsapi = NewsApiClient(api_key=NEWS_API)
    all_articles = newsapi.get_everything(q=q,
                                          from_param=from_param,
                                          language='en',
                                          sort_by='relevancy')
    top_three_articles = all_articles["articles"][:3]
    for item in range(0, len(top_three_articles)):
        news_title = top_three_articles[item]["title"]
        news_url = top_three_articles[item]["url"]
        msg = f"\nHeadline: {news_title}\nWebsite: {news_url}\n"
        MSG += msg


def calculate_stock_change():
    global MSG
    stock_change = round(
        (last_prev_stock_price - second_last_prev_stock_price) * 100 / last_prev_stock_price, 2
    )
    if (last_prev_stock_price >= second_last_prev_stock_price * 1.05
            or last_prev_stock_price <= second_last_prev_stock_price * 0.95):
        if stock_change > 0:
            msg = f"TSLA: 🔺{stock_change}%\n"
            MSG += msg
        elif stock_change < 0:
            msg = f"TSLA: 🔻{-stock_change}%\n"
            MSG += msg


def send_message():
    client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=MSG,
        from_="[TWILIO NUMBER]",
        to="[YOUR NUMBER]"
    )
    print(message.status)


stock_response = requests.get(url=STOCK_URL, params=stock_params)
stock_response.raise_for_status()

if int(DATE.strftime("%w")) == 0:
    last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{DAY_BEFORE_YESTERDAY}"]["4. close"]
    )
    second_last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{TWO_DAYS_AGO}"]["4. close"]
    )
    calculate_stock_change()
    get_news(q=COMPANY_NAME, from_param=DAY_BEFORE_YESTERDAY)
    send_message()
elif int(DATE.strftime("%w")) == 1:
    last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{TWO_DAYS_AGO}"]["4. close"]
    )
    second_last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{THREE_DAYS_AGO}"]["4. close"]
    )
    calculate_stock_change()
    get_news(q=COMPANY_NAME, from_param=TWO_DAYS_AGO)
    send_message()
else:
    last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{YESTERDAY}"]["4. close"]
    )
    second_last_prev_stock_price = float(
        stock_response.json()["Time Series (Daily)"][f"{DAY_BEFORE_YESTERDAY}"]["4. close"]
    )
    calculate_stock_change()
    get_news(q=COMPANY_NAME, from_param=YESTERDAY)
    send_message()
