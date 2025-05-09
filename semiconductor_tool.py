#!/usr/bin/bash





#my_functions_library


import numpy as np

#Constants
#q  Charge (C)

q = 1.602176634e-19 

# This dictionary stores values of relative permativity
REL_PERMITTIVITY = {
    'Si': 11.7,
    'GaAs': 12.5,
    'Ge': 16.1,
    'SiO2': 3.9,
    'HfO2': 25.0,
    'HfSiO4': 16.5,  
    'ZrO2': 22.5,    
}

#This function turns the relative permativity to a string
def get_rel_permativity(material: str) -> float:
    try:
        return REL_PERMITTIVITY[material]
    except KeyError:
        raise ValueError(f"Unknown material '{material}'. Available: {list(REL_PERMITTIVITY.keys())}")

#Electric conductivity
#Variables
#n is the electron concentration
#p is the hole concentration
#mu_e and mu_h are the mobilities for electrons and holes respectively

def conductivity(n: float, p: float, mu_e: float, mu_h: float) -> float:
    return q * (n * mu_e + p * mu_h)

#Mobility (calculated from conductivity)
#sigma is the conductivity
#cd is carrier density
def mobility(sigma: float, carrier_density: float) -> float:
    return sigma / (q * cd)

#drift carrier density
#E is energy 
def drift_cd(n: np.ndarray, mu: float, E: np.ndarray) -> np.ndarray:
    return q * n * mu * E

def trapezoidal_rule(fx: np.ndarray, x: np.ndarray) -> float:
    """
    Trapezoidal rule to be applied to current
    """
    N = len(x) - 1
    h = (x[-1] - x[0]) / N
    integral = 0.5 * (fx[0] + fx[-1]) * h
    for k in range(1, N):
        integral += fx[k] * h
    return integral

#j_e and j_h are the currents
#x and t is position and time
def current(j_e: np.ndarray, j_h: np.ndarray, x: np.ndarray, t: np.ndarray):
    I_e_t = np.zeros(len(t))
    I_h_t = np.zeros(len(t))

    for i in range(len(t)):
        I_e_t[i] = trapezoidal_rule_array(j_e[i], x)
        I_h_t[i] = trapezoidal_rule_array(j_h[i], x)

    Q_e = trapezoidal_rule_array(I_e_t, t)
    Q_h = trapezoidal_rule_array(I_h_t, t)

    return I_e_t, I_h_t, Q_e, Q_h

