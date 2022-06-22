
import streamlit as st
import yfinance as yf
import pandas as pd



st.write("""
#  Простое приложение для цен на акции
Показаны цена закрытия акций и объем продаж акцций Apple.
""")

#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2022-6-20')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st. run /my_streamlit/streamlit1.py
