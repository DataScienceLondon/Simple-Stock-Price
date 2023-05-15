# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st
import yfinance as yf
from PIL import Image

image = Image.open('https://github.com/DataScienceLondon/Simple-Stock-Price/blob/main/blob/master/LOGO.PNG')
st.image(image, use_column_width = True)

st.write('''
# Simple Stock Price Web App

Course developed by Chanin Nantasenamat (aka Data Professor). 
Check out his YouTube channel for more data science tutorials: https://www.youtube.com/c/DataProfessor

Shown are the stock **closing price** and **volume** of Google!        
         ''')

#Symbol         
tickerSymbol = 'GOOGL'
#Get tick data
tickerData = yf.Ticker(tickerSymbol)
#get historical prices
df_ticker = tickerData.history(period='1d',
                               start='2010-01-01',
                               end='2022-12-31'
                               )
# Open, High, Low Close, Volume, Dividends, Stock Splits
st.write('''
## Closing Price
''')
st.line_chart(df_ticker.Close)
st.write('''
## Volume
''')
st.line_chart(df_ticker.Volume)

