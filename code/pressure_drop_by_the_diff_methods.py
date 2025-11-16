import numpy as np
import matplotlib.pyplot as plt

#the parameters and viscosity expression

A = 2.58e-10
B = 7029.1

def mu(T):
    return A * np.exp(B / T)

#ref temp

T0 = 310   

#alpha

def alpha(T):
    return -B / T**2

# temp range

dT = np.linspace(0, 15, 400)

#linear

DP_lin = 1 + alpha(T0) * dT

#numerical

Nz = 1000
z = np.linspace(0, 1, Nz)   

DP_num = np.zeros_like(dT)

for j, DT in enumerate(dT):
    Tz = T0 + DT * z
    mu_z = mu(Tz)
    DP_num[j] = np.trapz(mu_z, z) / mu(T0)   

# louis ref

DP_louis = DP_lin.copy()

# plots

plt.figure(figsize=(9,6))
plt.plot(dT, DP_num, label="Nonlinear Numerical ΔP", linewidth=2)
plt.plot(dT, DP_lin, '--', label="Analytical Linearized ΔP", linewidth=2)
plt.plot(dT, DP_louis, ':', label="Louis et al. Asymptotic", linewidth=2)

plt.xlabel("Mean Temperature Rise ΔT (K)")
plt.ylabel("Normalized Pressure Drop ΔP / ΔP₀")
plt.title("Pressure Drop: Analytical vs Numerical Comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/pressure_drop_analytical_vs_numerical.png", dpi=300)
plt.show()

# deviation plot

err_lin = (DP_lin - DP_num) / DP_num * 100
err_louis = (DP_louis - DP_num) / DP_num * 100

plt.figure(figsize=(9,6))
plt.plot(dT, err_lin, label="Linear Model Error (%)")
plt.plot(dT, err_louis, '--', label="Louis et al. Error (%)")
plt.axhline(0, color='black', linewidth=0.7)

plt.xlabel("Mean Temperature Rise ΔT (K)")
plt.ylabel("Deviation from Numerical Nonlinear Model (%)")
plt.title("Deviation of Analytical Models from Numerical Pressure Drop")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/pressure_drop_error_vs_numerical.png", dpi=300)
plt.show()
