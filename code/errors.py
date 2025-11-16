
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Arrhenius parameters
A = 2.58e-10
B = 7029.1

T0 = 310.0
mu0 = A * np.exp(B/T0)

# ΔT range
dT_vals = np.linspace(0, 15, 60)
T_vals = T0 + dT_vals

# analytical soln
mu_analytical = A * np.exp(B / T_vals)
DP_analytical = mu_analytical / mu0

# numerical soln

def dDPdT(T, DP):
    """Derivative of ΔP/ΔP0 with respect to temperature."""
    muT = A * np.exp(B / T)
    dmu_dT = muT * (-B / T**2)  
    return dmu_dT / mu0

DP_num = []

for Tmax in T_vals:
    sol = solve_ivp(
        dDPdT,
        (T0, Tmax),
        y0=[1.0],       
        method='RK45',
        max_step=0.1
    )
    DP_num.append(sol.y[0, -1])

DP_num = np.array(DP_num)

# deviation calculation
error = 100 * (DP_analytical - DP_num) / DP_analytical

# anal vs numerical plot
plt.figure(figsize=(8,6))
plt.plot(dT_vals, DP_analytical, 'k-', linewidth=2, label="Analytical (Nonlinear Arrhenius)")
plt.plot(dT_vals, DP_num, 'r--', linewidth=2, label="Numerical (RK4 SolveIVP)")

plt.xlabel("ΔT (K)")
plt.ylabel("ΔP/ΔP₀")
plt.title("Analytical vs Numerical (RK4) Pressure-Drop Prediction")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/analytical_vs_numerical_pressure_drop.png", dpi=300)
plt.show()

#plotting error
plt.figure(figsize=(8,6))
plt.plot(dT_vals, error, 'b-', linewidth=2)
plt.axhline(0, color='k')
plt.xlabel("ΔT (K)")
plt.ylabel("Deviation (%)")
plt.title("Numerical Deviation from Analytical Nonlinear Solution")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/analytical_vs_numerical_error.png", dpi=300)
plt.show()

print("\nAnalytical vs Numerical comparison completed. Figures saved to 'figures/'.")
