# Main Page
import streamlit as st
import pandas as pd
import numpy as np
# Image Display
st.image('https://theforum.erf.org.eg/app/uploads/2020/03/1584990581_946_118839_corona4930541_1920.jpg', width=750)


# Add title
st.title('''EDA for Covid-19''')
st.header("World Health Orgnization")
st.markdown('''
#### COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.

##### Most common symptoms:
    - fever
    - cough
    - tiredness
    - loss of taste or smell.

##### Less common symptoms:
    - sore throat
    - headache
    - aches and pains
    - diarrhoea
    - a rash on skin, or discolouration of fingers or toes
    - red or irritated eyes.

##### Serious symptoms:
    - difficulty breathing or shortness of breath
    - loss of speech or mobility, or confusion
    - chest pain.

##### Recommendations :
- Seek immediate medical attention if you have serious symptoms.
- Always call before visiting your doctor or health facility. 
- People with mild symptoms who are otherwise healthy should manage their symptoms at home. 
- On average it takes 5 to 6 days from when someone is infected with the virus for symptoms to show, 
    however it can take up to 14 days. 
            ''')

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''#''')
        st.image('https://cdn.who.int/media/images/default-source/infographics/logo-who.tmb-1200v.jpg?sfvrsn=2fcc68a0_35', width=170)
