import streamlit as st
importpandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Crypto Performance", layout="wide")
st.title("Cryptocurrency Performance Dashboard")
st.markdown("Analyze and visualize the performance of various cryptocurrencies over selected time periods")

ALL = ["BTC-USD", "ETH-USD", "SOL-USD"]

with st.sidebar:
  st.header("Dashboard Settings")
  coins = st.multiselect("Choose coins", ALL, default=["BTC-USD", "ETH-USD", "SOL-USD"])
  start = st.date_input("Start date", pd.to_datetime("2022-01-01"))
  end = st.date_input("End date", pd.Timestamp.today())
  use_log = st.checkbox("Log scale (price)", value=False)

st.divider()

if not coins:
  st.warning("Select at least one cryptocurrency to get started")
  st.stop()

if start > end:
  st.error("Start date must be before end date")
  st.stop()

@st.cache_data(ttl=1800, show_spinner=False)
def load_prices(tickers, start, end):
  try:
    df = yf.download(tickers, start=start, end=end, progress=Flase)["Close"]
    if isintance(df, pd.Series):
      dt = df.to_frame()
    return dt.dropna(how="all")
  except Exception as e:
    st.error(f"Error loading data: {e}")
    return pd.DataFrame()
