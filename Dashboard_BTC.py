# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:19:21 2021

@author: edwin
"""

import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df_projected = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/BTC_risk_metric/891a1032cb63160763c33f235a4714f2083c9713/BTC_price_projections.csv")



st.title("""#BTC main Dashboard""")

st.line_chart(df_projected[["close"]])

#1.---API token definition
coin_name = "BTC"
projected_days = 180


#2.---Defines plotting parameters
#Background color
plt.style.use('dark_background')

#Plot size
plt.rcParams['figure.figsize'] = [16, 8]

#Price boundaries to plot
max_price_plot = 100000 
min_price_plot = 0.1


#3.---Plots regresion bands
fig, ax1 = plt.subplots()
plt.ylim(min_price_plot,max_price_plot*10)

ax1.set_title(coin_name + " prediction bands")
ax1.set_ylabel(coin_name + " price (USD)")

#Defines if logarithmic graph
log_val = True

#Plots regression bands
df_projected.plot(kind = "line", y = "plus_3STDV", logy=log_val, ax = ax1, secondary_y = False, c = "red", label="99.9%")
df_projected.plot(kind = "line", y = "plus_2STDV", logy=log_val, ax = ax1, secondary_y = False, c = "yellow", label="97.8%")
df_projected.plot(kind = "line", y = "plus_1STDV", logy=log_val, ax = ax1, secondary_y = False, c = "green", label="84.2%")
df_projected.plot(kind = "line", y = "price_reg", logy=log_val, ax = ax1, secondary_y = False, c = "grey", linestyle='dashed', label="50.0%")
df_projected.plot(kind = "line", y = "minus_1STDV", logy=log_val, ax = ax1, secondary_y = False, c = "green", label="15.8%")
df_projected.plot(kind = "line", y = "minus_2STDV", logy=log_val, ax = ax1, secondary_y = False, c = "yellow", label="2.2%")
df_projected.plot(kind = "line", y = "minus_3STDV", logy=log_val, ax = ax1, secondary_y = False, c = "red", label="0.1%")

#color bands
ax1.fill_between(df_projected.index, y1 = df_projected["plus_3STDV"], y2 = df_projected["plus_2STDV"], color='r', alpha=.2)
ax1.fill_between(df_projected.index, y1 = df_projected["plus_2STDV"], y2 = df_projected["plus_1STDV"], color='yellow', alpha=.2)
ax1.fill_between(df_projected.index, y1 = df_projected["minus_1STDV"], y2 = df_projected["plus_1STDV"], color='g', alpha=.2)
ax1.fill_between(df_projected.index, y1 = df_projected["minus_3STDV"], y2 = df_projected["minus_2STDV"], color='r', alpha=.2)
ax1.fill_between(df_projected.index, y1 = df_projected["minus_2STDV"], y2 = df_projected["minus_1STDV"], color='yellow', alpha=.2)

#Plots closing price
df_projected.plot(kind = "line", y = "close", logy=log_val, ax = ax1, secondary_y = False, c = "white", label= coin_name + " price")

#Creates grid
plt.grid(b=True, which = 'both', axis = 'both', alpha = 0.3)


st.pyplot(fig)
