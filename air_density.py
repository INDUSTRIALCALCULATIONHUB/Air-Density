import math
import streamlit as st

# Page setup
st.set_page_config(page_title="Air Density Calculator", layout="centered")

# Logo / Image
st.image("https://cdn-icons-png.flaticon.com/512/2933/2933245.png", width=80)

st.title("Air Density Calculator")

# Session state
if "altitude" not in st.session_state:
    st.session_state.altitude = ""
if "temperature" not in st.session_state:
    st.session_state.temperature = ""
if "result" not in st.session_state:
    st.session_state.result = None

# Inputs (NO +/- buttons)
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

    # ---- Pressure Units ----
    st.markdown("### Pressure")

    st.write(f"Pa     : {P:,.2f}")
    st.write(f"kPa    : {P/1000:,.3f}")
    st.write(f"bar    : {P/100000:,.5f}")
    st.write(f"atm    : {P/101325:,.5f}")
    st.write(f"mmWC   : {P/9.80665:,.2f}")

    # ---- Density Units ----
    st.markdown("### Density")

    st.write(f"kg/m³  : {rho:.4f}")
    st.write(f"g/cm³  : {rho/1000:.6f}")
    st.write(f"lb/ft³ : {rho*0.062428:.4f}")
    st.write(f"slug/ft³ : {rho*0.00194032:.6f}")
    st.write(f"kg/L   : {rho/1000:.6f}")