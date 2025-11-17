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
