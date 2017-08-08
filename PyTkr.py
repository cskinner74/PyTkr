#!/usr/bin/python
#Created by Cody Skinner

import argparse
import sys
import ConfigParser
import json
import requests
import ast
import time
from datetime import datetime, timedelta

#Parser for command line arguments
parser = argparse.ArgumentParser(description="Check for stock ticker information from the command line.")
parser.add_argument("ticker", help="Ticker symbol")
args = parser.parse_args()
ticker = args.ticker.upper()

#Parser for config file
config = ConfigParser.ConfigParser()
config.read("config.py")
apikey = config.get('API', 'apikey')

#API information
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ticker+"&apikey="+apikey
response = requests.get(url)
data = response.json()

#Date formatting for JSON
now = datetime.now()
#Previous date
date2 = now.date() - timedelta(days=1)
date = str(date2) #Convert to string

#get data
openprice = data["Time Series (Daily)"][date]["1. open"] #get open price
openprice = float(openprice) #convert to float
openprice = "{0:.2f}".format(openprice) #round to 2 decimal places
high = data["Time Series (Daily)"][date]["2. high"]
high = float(high)
high="{0:.2f}".format(high)
low = data["Time Series (Daily)"][date]["3. low"]
low = float(low)
low = "{0:.2f}".format(low)
close = data["Time Series (Daily)"][date]["4. close"] 
close = float(close)
close = "{0:.2f}".format(close)


#output
print "End of day data for %s on %s:" %(ticker, date)
print "Open: $"+openprice
print "High: $"+high
print "Low: $"+low
print "Close: $"+close
