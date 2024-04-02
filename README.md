# Financial News Alert System

The Financial News Alert System is a Python application designed to monitor stock price changes of a specific company (in this case, Tesla Inc.) and send relevant news articles as SMS alerts. It utilizes the Alpha Vantage API for stock price data, the NewsAPI for fetching news articles related to the stock's company, and Twilio's API for sending SMS messages.

## Features

- Monitors stock price changes for Tesla Inc. (TSLA) over the last trading days.
- Fetches news articles related to Tesla Inc. if the stock price has significant changes (increase or decrease by 5% or more).
- Sends an SMS alert with the stock price change and top news headlines using Twilio's SMS API.

## Prerequisites

To use the Financial News Alert System, you will need:

- Python 3.x
- A free API key from Alpha Vantage for stock data.
- A free API key from NewsAPI for news articles.
- A Twilio account with an Auth Token, Account SID, and a Twilio phone number.

## Setup

1. **Clone or download this repository** to your local machine.
2. **Install required Python libraries** by running the following command:
   ```bash
   pip install newsapi-python twilio requests
   ```
3. **Obtain your API keys**:
   - Sign up for Alpha Vantage and obtain your API key.
   - Sign up for NewsAPI and obtain your API key.
   - Sign up for Twilio, purchase an SMS-capable phone number, and obtain your Account SID and Auth Token.
4. **Configure the script with your API keys and Twilio information**:
   - Replace the placeholder values for `ALPHA_VANTAGE_API`, `NEWS_API`, `TWILIO_ACCOUNT_SID`, and `TWILIO_AUTH_TOKEN` in the script with your actual API keys and Twilio credentials.
   - Ensure you also set the `to` and `from_` parameters in the `send_message` function to match your Twilio phone number and the recipient's phone number.

## Running the System

Run the script with the following command:

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of the main script file if it's different.

The system will automatically check for stock price changes of Tesla Inc. If the price has changed significantly since the previous trading day, it will fetch the latest news articles related to Tesla and send an SMS alert to the specified phone number.

## Customization

To monitor a different company:

- Change the `STOCK` variable to the symbol of the company you're interested in.
- Update the `COMPANY_NAME` variable accordingly.

Remember to respect API rate limits and terms of use when customizing and running your script.
