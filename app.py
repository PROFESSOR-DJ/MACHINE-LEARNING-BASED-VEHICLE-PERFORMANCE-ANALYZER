import pandas as pd
import joblib
import streamlit as st
model = joblib.load('new_vehicle_mileage_model.pkl')
st.markdown(
    """
    <style>
    /* Hide Streamlit's header */
    header {
        visibility: hidden;
    }
    /* Hide Streamlit's footer */
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title('Vehicle Mileage Analyzer')

st.sidebar.header('Input Parameters')
engine_size = st.sidebar.number_input(
    'Engine Size (cc)', min_value=500, max_value=10000, step=100, value=2000)
horsepower = st.sidebar.number_input(
    'Horsepower (hp)', min_value=50, max_value=1000, step=10, value=180)
torque = st.sidebar.number_input(
    'Torque (Nm)', min_value=50, max_value=2000, step=10, value=250)
weight = st.sidebar.number_input(
    'Weight (kg)', min_value=500, max_value=5000, step=100, value=1300)

def predict_mileage_per_liter(engine_size, horsepower, torque, weight):
    sample_vehicle = [[engine_size, horsepower, torque, weight]]
    predicted_mileage = model.predict(sample_vehicle)
    return predicted_mileage[0]


predicted_mileage_per_liter = predict_mileage_per_liter(
    engine_size, horsepower, torque, weight)

fuel_efficiency_for_1_km = 1 / predicted_mileage_per_liter


def check_performance(mileage, fuel_efficiency):
    mileage_threshold = 12 
    
    fuel_efficiency_threshold = 0.08

    is_mileage_good = mileage >= mileage_threshold
    is_fuel_efficiency_good = fuel_efficiency <= fuel_efficiency_threshold

    return is_mileage_good, is_fuel_efficiency_good



is_mileage_good, is_fuel_efficiency_good = check_performance(
    predicted_mileage_per_liter, fuel_efficiency_for_1_km)


st.header('Predicted Mileage per Liter (km/l)')
st.markdown(
    f'<h1 style="text-align: center;">{predicted_mileage_per_liter:.2f} km/l</h1>', unsafe_allow_html=True)


st.header('Fuel Efficiency for 1 Kilometer')

st.markdown(
    f'<h1 style="text-align: center;">{fuel_efficiency_for_1_km:.2f} liters of fuel per kilometer</h1>', unsafe_allow_html=True)


st.header('Performance Evaluation')
if is_mileage_good and is_fuel_efficiency_good:
    st.success(
        'Both mileage and fuel efficiency are good for the vehicle\'s configuration.')
elif is_mileage_good:
    st.info('Mileage is good, but fuel efficiency is not ideal.')
elif is_fuel_efficiency_good:
    st.info('Fuel efficiency is good, but mileage is not ideal.')
else:
    st.warning(
        'Both mileage and fuel efficiency are not ideal for the vehicle\'s configuration.')
