import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# this loads the dataset from the data folder

df = pd.read_csv("data/raw_ramirez_viscosity_data.csv")

T = df["Temperature_K"].values
mu = df["Viscosity_Pa_s"].values

#definiung the axes for the plot

x = 1.0 / T           # 1/T
y = np.log(mu)        # ln(mu)

#fitting the linearized Arrhenius model

def linear_model(x, lnA, B):
    return lnA + B * x

popt, pcov = curve_fit(linear_model, x, y)
lnA_fit, B_fit = popt

A_fit = np.exp(lnA_fit)

print("\n===== Linearized Arrhenius Fit =====")

print(f"A     = {A_fit:.4e}")
print(f"B     = {B_fit:.2f}")

# Generates the fit

x_fit = np.linspace(min(x), max(x), 400)
y_fit = linear_model(x_fit, lnA_fit, B_fit)

#plots it

plt.figure(figsize=(9,6))
plt.scatter(x, y, s=40, label="Data")
plt.plot(x_fit, y_fit, 'r-', linewidth=2,
         label=f"Fit: ln(μ) = {lnA_fit:.2f} + ({B_fit:.1f})/T")

plt.xlabel("1 / T (1/K)")
plt.ylabel("ln(μ)")
plt.title("Arrhenius Fit of μ–T Data (Linearized Form)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/arrhenius_linearized.png", dpi=300)
plt.show()

#finding R^2

y_pred = linear_model(x, lnA_fit, B_fit)

SS_res = np.sum((y - y_pred)**2)
SS_tot = np.sum((y - np.mean(y))**2)

R2 = 1 - (SS_res / SS_tot)

print(f"R^2 = {R2:.5f}")