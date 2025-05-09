#!/usr/bin/bash







import my_function_lib as mfl

#These are exampls of user settings.
#Test case
if __name__ == '__main__':
    n0 = 1e16 #Equilibrium e- concentration (cm^(-3))
    p0 = 1e10 #Equilibrium h+ concentration (cm^(-3))
    g = 1e21 # Generation rate (cm^(-3) s^(-1))

    x = np.linspace(0, 1e-3, 1000) #Example of spatial grid
    t = np.linspace(0, 1e-5, 500) #Example of time grid
    n_prime = np.zeros((len(t), len(x))) #excess e-
    p_prime = np.zeros((len(t), len(x))) #excess h+

    n = n0 + n_prime #total electron density
    p = p0 + p_prime # total h+ density
    E = 1e3 * np.ones_like(n)

    material = 'GaAs' #example of silicon as material
    eps_r = mfl.get_rel_permativity(material) #finding permitivity

    mu_e = 1300  #e- mobility (cm^2/Vs)
    mu_h = 500   # h+ mobility(cm^2/Vs)
    sigma = mfl.conductivity(n0, p0, mu_e, mu_h)
    print(f"Conductivity in {material}: {sigma:.2e} S/cm (using n0, p0, mu_e, mu_h)")

    # Drift current density
    j_e = mfl.drift_cd(n, mu_e, E)# e- drift current density
    j_h = mfl.drift_cd(p, mu_h, E) # h+ drift current density

    # Print Output
    I_e_t, I_h_t, Q_e, Q_h = mfl.current(j_e, j_h, x, t)
    print(f"Electron current: {np.max(I_e_t):.2e} A/cm")
    print(f"Transported e- Charge: {Q_e:.2e} C/cm")
    print(f"Hole Current: {np.max(I_h_t):.2e} A/cm")
    print(f"Transported h+ Charge: {Q_h:.2e} C/cm")
