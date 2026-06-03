import math
import streamlit as st

# Page config
st.set_page_config(page_title="Air Density Calculator", layout="centered")

st.title("Air Density Calculator")
st.write("Calculate atmospheric pressure and air density based on altitude and temperature")

# Inputs
altitude = st.number_input("Altitude (m above MSL)", value=0.0, step=10.0)
temperature = st.number_input("Gas Temperature (°C)", value=25.0, step=1.0)

# Constants
P0 = 101325        # Pa
T0 = 288.16        # K
L = 0.0065         # K/m
g = 9.80665        # m/s²
M = 0.0289644      # kg/mol
R = 8.314462618    # J/mol·K
R_specific = 287.058  # J/kg·K

# Buttons
col1, col2 = st.columns(2)

# Calculate button
if col1.button("Calculate"):
    try:
        # Pressure using ISA model
        exponent = (g * M) / (R * L)
        P = P0 * (1 - (L * altitude) / T0) ** exponent

        # Convert temperature to Kelvin
        T = temperature + 273.15

        # Density calculation
        rho = P / (R_specific * T)

        # Output
        st.subheader("Results")
        st.success(f"Atmospheric Pressure: {P:,.2f} Pa")
        st.success(f"Air Density: {rho:.3f} kg/m³")

    except Exception as e:
        st.error("Error in calculation. Please check inputs.")

# Reset button
if col2.button("Reset"):
    st.session_state.clear()
    st.rerun()