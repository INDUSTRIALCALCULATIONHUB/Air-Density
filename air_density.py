import math
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Air Density Calculator", layout="centered")

# Engineering icon (air / fluid)
st.image("https://cdn-icons-png.flaticon.com/512/4149/4149643.png", width=80)

st.title("Air Density Calculator")

# Session state
if "altitude" not in st.session_state:
    st.session_state.altitude = ""
if "temperature" not in st.session_state:
    st.session_state.temperature = ""
if "result" not in st.session_state:
    st.session_state.result = None

# Inputs (no +/- buttons)
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

# Calculate
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

# Reset
if col2.button("Reset"):
    st.session_state.altitude = ""
    st.session_state.temperature = ""
    st.session_state.result = None
    st.rerun()

# Output
if st.session_state.result:
    P, rho = st.session_state.result

    st.subheader("Results")

    # ---- Pressure Table ----
    pressure_df = pd.DataFrame({
        "Unit": ["Pa", "kPa", "bar", "atm", "mmWC"],
        "Value": [
            f"{P:.2f}",
            f"{P/1000:.2f}",
            f"{P/100000:.2f}",
            f"{P/101325:.2f}",
            f"{P/9.80665:.2f}"
        ]
    })

    st.markdown("### Pressure")
    st.dataframe(pressure_df, use_container_width=True, hide_index=True)

    # ---- Density Table ----
    density_df = pd.DataFrame({
        "Unit": ["kg/m³", "g/cm³", "lb/ft³", "slug/ft³", "kg/L"],
        "Value": [
            f"{rho:.2f}",
            f"{rho/1000:.2f}",
            f"{rho*0.062428:.2f}",
            f"{rho*0.00194032:.2f}",
            f"{rho/1000:.2f}"
        ]
    })

    st.markdown("### Density")
    st.dataframe(density_df, use_container_width=True, hide_index=True)