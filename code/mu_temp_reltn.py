import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this loads the dataset 

df = pd.read_csv("data/raw_ramirez_viscosity_data.csv")

T = df["Temperature_K"].values
mu = df["Viscosity_Pa_s"].values

# Arrhenius parameters which we got from regression

A = 2.58e-10
B = 7029.1

def mu_arrhenius(T):
    return A * np.exp(B / T)

# curve
T_fit = np.linspace(min(T), max(T), 400)
mu_fit = mu_arrhenius(T_fit)

plt.figure(figsize=(9,6))
plt.scatter(T, mu, s=45, label="Experimental Data")
plt.plot(T_fit, mu_fit, 'r-', linewidth=2, label="Arrhenius Fit")
plt.yscale("log")
plt.xlabel("Temperature (K)")
plt.ylabel("Viscosity μ(T) (Pa·s)")
plt.title("Viscosity–Temperature Relation (Arrhenius Law)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/mu_vs_T.png", dpi=300)
plt.show()
