
```markdown
# CLL-110 Term Paper Appendix  
### *Modeling Temperature-Dependent Viscosity Effects in Crude Oil Pipeline Transport*  
**Course:** CLL-110 (Transport Phenomena)  
**Institution:** IIT Delhi  


## Overview

This repository contains all datasets, scripts, and figures used in the term paper:

“Modeling Temperature-Dependent Viscosity Effects in Crude Oil Pipeline Transport:  
An Arrhenius-Based Analytical Framework.”

The purpose of this repository is to make the entire analysis fully reproducible, including:

- Arrhenius viscosity regression  
- Analytical pressure-drop derivation  
- Numerical verification of the nonlinear pressure-drop integral  
- Comparison with the asymptotic model of Louis, Boyko & Stone (2023)  
- All plots included in the paper  

No CFD or external simulation tools are used here; the paper focuses on a coupled analytical–numerical validation of viscosity-dependent laminar pipe flow.



## Repository Skeleton


.
├── data/
│   └── raw_ramirez_viscosity_data.csv
│
├── figures/
│   ├── arrhenius_linearized.png
│   ├── mu_vs_T.png
│   ├── pressure_drop_analytical_vs_numerical.png
│   └── pressure_drop_error_vs_numerical.png
│
├── code/
│   ├── 01_arrhenius_linearized_plot.py
│   ├── 02_mu_vs_T_plot.py
│   ├── 03_pressure_drop_comparison.py
│   └── 05_pressure_drop_analytical_vs_numerical.py
│
└── README.md

````

##  Included Scripts & What They Output

###  regression_fit.py
- Fits the Arrhenius law  
  \[
  \mu(T) = A \exp(B/T)
  \]
  using linear regression on ln(μ) vs 1/T.
- Computes:
  - A, B  
  - 95% confidence intervals  
  - Coefficient of determination (R²)
- Generates the linearized Arrhenius plot used in the paper.

---

### mu_temp_reltn.py
- Plots viscosity vs temperature on a log-scale.
- Overlays the nonlinear Arrhenius curve.
- Demonstrates how viscosity decreases exponentially with temperature.

---

### pressure_drop_by_the_diff_methods.py
- Produces the pressure-drop comparison figure in the Results section:
  - True nonlinear model (Arrhenius)
  - Linearized analytical model  
  - Louis et al. (2023) asymptotic model  
- Computes percent deviation between the three.

This figure is included in the paper's validation section.

---

### errors.py

- Numerically solves the pressure–drop relation using a Runge–Kutta (RK45) ODE solver (solve_ivp)

- Computes the full nonlinear analytical Arrhenius model

- Computes the linearized analytical model

- Computes the Louis–Boyko–Stone asymptotic model



- Generates:

    - Normalized pressure–drop comparison plot

    

-This script provides the numerical verification used in the paper to confirm the correctness of the analytical Arrhenius-based pressure–drop expression.

---

## Dataset

The data used for Arrhenius regression comes directly from:

**Ramírez et al. (2023)**  
*Prediction of Temperature and Viscosity Profiles in Heavy-Oil Producer Wells*  
Processes 11(2), 631.

The dataset contains 16 temperature–viscosity pairs for API ≈ 12 heavy crude.  
The values were taken directly from the published supplementary material (no digitization).

---

##  How to Run the Scripts

1. Ensure Python 3.8+ is installed.
2. Install required packages:
   ```bash
   pip install numpy pandas matplotlib scipy
````

3. Run any script from the `code/` directory, e.g.:

   ```bash
   python errors.py
   ```
4. Generated figures will appear automatically in the `figures/` directory.

---

## Outputs (Figures Included)

All scripts automatically store figures in:

```
figures/
```

These include:

* Arrhenius linearized regression curve
* μ(T) nonlinear Arrhenius curve
* Pressure-drop comparison: nonlinear vs linear vs asymptotic
* Error (%) between models

Every figure corresponds exactly to what is shown in the term paper.

---




