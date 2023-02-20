import streamlit as st
import pandas as pd

# Load Data :


def load_data():
    df = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv")
    pd.options.display.float_format = '{:,.0f}'.format
    df["Date_reported"] = pd.to_datetime(df["Date_reported"])
    return df


df = load_data()

st.title('About Data')
st.markdown('''
### EDA for Covid-19 created based on World Health Orgnization Data
#### Source of data :
- Website : www.who.int
- World Health Orgnization
''')
st.markdown('''
|Field name|	Type	|Description|
|----------|--------|-----------|
|Date_reported	|Date	|Date of reporting to WHO|
|Country_code	|String	|ISO Alpha-2 country code|
|Country	|String	|Country, territory, area|
|WHO_region	|String	|WHO regional offices:WHO Member States are grouped into six WHO regions -- Regional Office for Africa (AFRO), Regional Office for the Americas (AMRO), Regional Office for South-East Asia (SEARO), Regional Office for Europe (EURO), Regional Office for the Eastern Mediterranean (EMRO), and Regional Office for the Western Pacific (WPRO).
|New_cases	|Integer	|New confirmed cases. Calculated by subtracting previous |cumulative case count from current cumulative cases count.*|
|Cumulative_cases	|Integer	|Cumulative confirmed cases reported to WHO to date.|
|New_deaths	|Integer	|New confirmed deaths. Calculated by subtracting previous ||cumulative deaths from current cumulative deaths.*|
|Cumulative_deaths	|Integer	|Cumulative confirmed deaths reported to WHO to date.|
''')

# Disply Data
st.header('Data View')
Data_Options = st.selectbox(
    'Select Option :', ['Select', 'Data', 'Sample', 'Describe'])
if Data_Options == 'Select':
    st.subheader('Select from list')
elif Data_Options == 'Data':
    st.subheader('Data Show :')
    st.write(df)
elif Data_Options == 'Sample':
    st.subheader("Sample 5 Rows from Data :")
    st.write(df.sample(5))
else:
    st.subheader("Describe Data :")
    st.write(df.describe())
