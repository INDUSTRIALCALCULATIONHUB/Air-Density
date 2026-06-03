import math
import tkinter as tk
from tkinter import messagebox

# Function to calculate density
def calculate():
    try:
        altitude = float(entry_altitude.get())
        temp_c = float(entry_temp.get())

        # Constants
        P0 = 101325
        T0 = 288.16
        L = 0.0065
        g = 9.80665
        M = 0.0289644
        R = 8.314462618
        R_specific = 287.058

        # Pressure (ISA model)
        exponent = (g * M) / (R * L)
        P = P0 * (1 - (L * altitude) / T0) ** exponent

        # Temperature in Kelvin
        T = temp_c + 273.15

        # Density
        rho = P / (R_specific * T)

        # Display results
        result_pressure.config(text=f"{P:.2f} Pa")
        result_density.config(text=f"{rho:.3f} kg/m³")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")


# Function to reset inputs
def reset():
    entry_altitude.delete(0, tk.END)
    entry_temp.delete(0, tk.END)
    result_pressure.config(text="")
    result_density.config(text="")


# Create window
root = tk.Tk()
root.title("Air Density Calculator")
root.geometry("350x250")

# Labels and Inputs
tk.Label(root, text="Altitude (m):").pack(pady=5)
entry_altitude = tk.Entry(root)
entry_altitude.pack()

tk.Label(root, text="Temperature (°C):").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate, bg="lightgreen").pack(pady=10)
tk.Button(root, text="Reset", command=reset, bg="lightcoral").pack()

# Results
tk.Label(root, text="Pressure:").pack(pady=5)
result_pressure = tk.Label(root, text="", fg="blue")
result_pressure.pack()

tk.Label(root, text="Density:").pack(pady=5)
result_density = tk.Label(root, text="", fg="blue")
result_density.pack()

# Run app
root.mainloop()