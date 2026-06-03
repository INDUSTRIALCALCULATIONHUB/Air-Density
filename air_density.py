import math
import streamlit as st

st.set_page_config(page_title="Air Density Calculator")

st.title("Air Density Calculator")

# Initialize session state for inputs
if "altitude" not in st.session_state:
    st.session_state.altitude = ""
if "temperature" not in st.session_state:
    st.session_state.temperature = ""
if "result" not in st.session_state:
    st.session_state.result = None

# Input fields (TEXT → no +/- buttons)
altitude = st.text_input("Altitude (m above MSL)", value=st.session_state.altitude)
temperature = st.text_input("Gas Temperature (°C)", value=st.session_state.temperature)

# Constants
P0 = 101325
T0 = 288.16
L = 0.0065
g = 9.80665
M = 0.0289644
R = 8.314462618
R_specific = 287.058

# Buttons
col1, col2 = st.columns(2)

# Calculate button
if col1.button("Calculate"):
    try:
        altitude_val = float(altitude)
        temp_val = float(temperature)

        exponent = (g * M) / (R * L)
        P = P0 * (1 - (L * altitude_val) / T0) ** exponent

        T = temp_val + 273.15
        rho = P / (R_specific * T)

        st.session_state.result = (P, rho)

    except:
        st.error("Please enter valid numeric values")

# Reset button
if col2.button("Reset"):
    st.session_state.altitude = ""
    st.session_state.temperature = ""
    st.session_state.result = None
    st.rerun()

# Show results ONLY after calculation
if st.session_state.result:
    P, rho = st.session_state.result

    st.subheader("Results")
    st.success(f"Atmospheric Pressure: {P:,.2f} Pa")
    st.success(f"Air Density: {rho:.3f} kg/m³")