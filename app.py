import streamlit as st 
import pandas as pd 
import joblib

#Load model
model = joblib.load("C:/Users/Yashasri/Desktop/AV/random_forest_model.pkl")

st.set_page_config(page_title="EV Charging Efficiency Predictor", layout="centered") 
st.title("🔋 EV Charging Efficiency Predictor") 
st.markdown("Predict the charging efficiency (kWh/min) of an EV charging session.")

#Input sliders
battery_capacity = st.slider("Battery Capacity (kWh)", 10.0, 150.0, 60.0, 1.0) 
charging_duration = st.slider("Charging Duration (mins)", 1, 300, 45, 1) 
energy_delivered = st.slider("Energy Delivered (kWh)", 1.0, 100.0, 20.0, 0.5) 
charging_cost = st.slider("Charging Cost ($)", 0.0, 100.0, 10.0, 0.5) 
temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0, 0.5) 
station_utilization = st.slider("Station Utilization Rate (%)", 0.0, 100.0, 50.0, 1.0)

#Create input DataFrame
input_data = pd.DataFrame({ 'Battery Capacity (kWh)': [battery_capacity], 'Charging Duration (mins)': [charging_duration], 'Energy Delivered (kWh)': [energy_delivered], 'Charging Cost ($)': [charging_cost], 'Temperature (°C)': [temperature], 'Station Utilization Rate (%)': [station_utilization] })

#Predict
if st.button("Predict Efficiency"): 
    prediction = model.predict(input_data)[0] 
    st.success(f"⚡ Predicted Charging Efficiency: {prediction:.3f} kWh/min")

#Footer
st.markdown("---") 
st.markdown("Made with ❤️ using Streamlit | by Yashasri")