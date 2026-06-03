import math

def air_density(altitude_m, temp_c):
    """
    Calculate air density based on altitude and gas temperature.

    Inputs:
    altitude_m : Altitude in meters (from MSL)
    temp_c     : Gas temperature in degree Celsius

    Returns:
    density (kg/m3), pressure (Pa)
    """

    # Constants
    P0 = 101325        # Sea level pressure (Pa)
    T0 = 288.16        # Sea level temperature (K)
    L = 0.0065         # Lapse rate (K/m)
    g = 9.80665        # Gravity (m/s2)
    M = 0.0289644      # Molar mass of air (kg/mol)
    R = 8.314462618    # Universal gas constant (J/mol.K)
    R_specific = 287.058  # Specific gas constant (J/kg.K)

    # Step 1: Calculate pressure using ISA model
    exponent = (g * M) / (R * L)
    P = P0 * (1 - (L * altitude_m) / T0) ** exponent

    # Step 2: Convert temperature to Kelvin
    T = temp_c + 273.15

    # Step 3: Calculate density
    rho = P / (R_specific * T)

    return rho, P


# Example usage
altitude = 400       # meters
temperature = 60     # deg C

density, pressure = air_density(altitude, temperature)

print(f"Pressure: {pressure:.2f} Pa")
print(f"Density : {density:.3f} kg/m3")