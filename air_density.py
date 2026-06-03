import math
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Air Density Calculator", layout="centered")

# Logo
st.image(
    "https://cdn-icons-png.flaticon.com/512/1684/1684375.png",
    width=90
)

st.title("Air Density Calculator")

# Constants
P0 = 101325
T0 = 288.16
L = 0.0065
g = 9.80665
M = 0.0289644
R = 8.314462618
R_specific = 287.058

# Result storage
if "result" not in st.session_state:
    st.session_state.result = None

# ================= FORM (FIX FOR RESET ISSUE) =================
with st.form("calc_form"):

    altitude = st.text_input("Altitude (m above MSL)")
    temperature = st.text_input("Gas Temperature (°C)")

    col1, col2 = st.columns(2)

    calculate = col1.form_submit_button("Calculate")
    reset = col2.form_submit_button("Reset")

    # CALCULATE
    if calculate:
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

    # RESET (FORM SAFETY → NO SESSION STATE ERROR)
    if reset:
        st.session_state.result = None
        st.rerun()

# ================= OUTPUT =================
if st.session_state.result:
    P, rho = st.session_state.result

    st.subheader("Results")

    # Pressure table
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

    # Density table
    density_df = pd.DataFrame({
        "Unit": ["kg/m³", "lb/ft³"],
        "Value": [
            f"{rho:.2f}",
            f"{rho * 0.062428:.2f}"
        ]
    })

    st.markdown("### Density")
    st.dataframe(density_df, use_container_width=True, hide_index=True)