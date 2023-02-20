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
df = helper.load_data()

# intro :
st.title("Covid-19 EDA")
st.markdown('''EDA By Contries for Covid-19''')

# Country Selection :
contry_options = st.selectbox(
    'Select Contry', ['All Contries', 'Select Contries'])
if contry_options == 'All Contries':
    contries = 'All Contries'
else:
    contries = st.multiselect('Select', df['Country'].unique())

# Date Selection :
# Start Date
start_date = st.date_input('Start date', df.Date_reported.min())
start_date = pd.to_datetime(start_date)
# End Date
end_date = st.date_input('End date ', df.Date_reported.max())
end_date = pd.to_datetime(end_date)

# Display total cases
st.header('Total Cases per contries')
total_cases = helper.contries_total_case(contries, start_date, end_date)
st.plotly_chart(total_cases)

# Display total deaths
st.header('Total Deaths per contries')
total_deaths = helper.contries_total_deaths(contries, start_date, end_date)
st.plotly_chart(total_deaths)
