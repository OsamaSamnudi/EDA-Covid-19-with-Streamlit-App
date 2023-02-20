import helper
import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load Data :
@st.cache_data

def load_data():
    df = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv")
    pd.options.display.float_format = '{:,.0f}'.format
    df["Date_reported"] = pd.to_datetime(df["Date_reported"])
    return df


df = load_data()

# Total (Cases,Deaths per Region (A)/Countries(B))
# Step 1) Add the Function to Helper
# Step 2) call the functionfrom helper in dusplayes page with "Helper Fuciton"

df.columns
# A) Total Cases/Total Deaths per Region :
# 1-A) Total Cases


def regions_total_cases(regions, start_date=df.Date_reported.min(), end_date=df.Date_reported.max()):
    if regions != 'All Regions':
        df_temp = df[df['WHO_region'].isin(regions)]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_cases',
                       title='Total Cases in Regions', range_x=[start_date, end_date], nbins=50)
    return fig
# 2-A) Total Deaths


def regions_total_deaths(regions, start_date=df.Date_reported.min(), end_date=df.Date_reported.max()):
    if regions != 'All Regions':
        df_temp = df[df['WHO_region'].isin(regions)]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_deaths',
                       title='Total Deaths in Regions', range_x=[start_date, end_date], nbins=50)
    return fig

# B) Total Cased/Total Deaths per contries
# 1-B) Total case per contries


def contries_total_case(contries, start_date=df.Date_reported.min(), end_date=df.Date_reported.max()):
    if contries != 'All Contries':
        df_temp = df[df['Country'].isin(contries)]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_cases',
                       title='Total Cases in Contries', range_x=[start_date, end_date], nbins=50)
    return fig
# 2-B) Total Deaths per contries


def contries_total_deaths(contries, start_date=df.Date_reported.min(), end_date=df.Date_reported.max()):
    if contries != 'All Contries':
        df_temp = df[df['Country'].isin(contries)]
    else:
        df_temp = df
    fig = px.histogram(df_temp, x='Date_reported', y='New_deaths',
                       title='Total Deaths in Countries', range_x=[start_date, end_date], nbins=50)
    return fig
