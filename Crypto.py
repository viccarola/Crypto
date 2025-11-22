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
