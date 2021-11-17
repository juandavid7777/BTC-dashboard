# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:19:21 2021

@author: Juan
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime


#1.-----Downloads data
df = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/BTC_risk_metric/891a1032cb63160763c33f235a4714f2083c9713/BTC_price_projections.csv")


#2.-----API token definition
coin_name = "BTC"
projected_days = 180


#3.-----Plots figures

fig = go.Figure()

#Price candlesticks plots
fig.add_trace(go.Candlestick(
    x=df['Date'],
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name = coin_name + ' price'
    ))

#Prices for uncertainity bands
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["plus_3STDV"],
    mode = 'lines',
    name = '99.9%',
    line = dict(width = 1.5, dash = 'dash', color = "red")
    ))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["plus_2STDV"],
    mode = 'lines',
    name = '97.8%',
    line = dict(width = 1.5, dash = 'dash', color = "yellow")
    ))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["plus_1STDV"],
    mode = 'lines',
    name = '84.2%',
    line = dict(width = 1.5, dash = 'dash', color = "green")
    ))

#Prices regression plot
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["price_reg"],
    mode = 'lines',
    name = '50.0%',
    line = dict(width = 1.5, dash = 'dash', color = "grey")
    ))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["minus_1STDV"],
    mode = 'lines',
    name = '15.8%',
    line = dict(width = 1.5, dash = 'dash', color = "green")
    ))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["minus_2STDV"],
    mode = 'lines',
    name = '2.2%',
    line = dict(width = 1.5, dash = 'dash', color = "yellow")
    ))

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df["minus_3STDV"],
    mode = 'lines',
    name = '0.1%',
    line = dict(width = 1.5, dash = 'dash', color = "red")
    ))

#Defines the y axis log scale
fig.update_layout(
    title = coin_name + " uncertainity bands",
    plot_bgcolor = "black",
    yaxis_type="log",
    xaxis_rangeslider_visible=False)

st.plotly_chart(fig)
