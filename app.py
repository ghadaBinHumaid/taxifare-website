import streamlit as st
import requests
from datetime import datetime, date, time


st.title(" TaxiFareModel front")


st.markdown('''
Use the controls below to set your ride parameters.
''')

col1, col2 = st.columns(2)
with col1:
    d = st.date_input("Pickup date", value=date(2014, 7, 6))
with col2:
    t = st.time_input("Pickup time", value=time(19, 18))

col3, col4 = st.columns(2)
with col3:
    pickup_longitude = st.number_input("Pickup longitude", value=-73.950655, format="%.6f")
    dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365, format="%.6f")
with col4:
    pickup_latitude = st.number_input("Pickup latitude", value=40.783282, format="%.6f")
    dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802, format="%.6f")

passenger_count = st.number_input("Passenger count", min_value=1, max_value=8, value=2, step=1)
pickup_datetime = datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")

url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": int(passenger_count),
}

resp = requests.get(url, params=params, timeout=15)
data = resp.json()
fare = data.get("fare", None)
st.write("The prediction is:", fare)
