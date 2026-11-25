import streamlit as st
import requests
import secrets

"""
# Zoologist front
"""

st.markdown("""

    ## What species is this penguin?

    Choose the island, adjust the bill and fin measurements as well as the weight, and select the sex to view the prediction."""
)

islands = ['Biscoe', 'Dream', 'Torgersen']
gender = ['Male', 'Female']

option = st.selectbox('Select an island', islands)

bill_length = st.number_input('Insert bill length (in mm)')
bill_depth = st.number_input('Insert bill depth (in mm)')
flipper_length = st.number_input('Insert flipper length (in mm)')
body_mass = st.number_input('Insert body mass (in g)')

option2 = st.selectbox('Select the gender', gender)

base_url = st.secrets['API_URL']

params = {
    'island' : option,
    'bill_length_mm' : bill_length,
    'bill_depth_mm' : bill_depth,
    'flipper_length_mm' : flipper_length,
    'body_mass_g' : body_mass,
    'sex' : option2
    }

response = requests.get(base_url, params = params)

if response.status_code == 200:
    data = response.json()
    result = data['prediction']
    st.write(result)
