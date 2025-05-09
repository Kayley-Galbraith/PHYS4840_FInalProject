# Semiconductor_tool
Final project for phys 4840





---

## Table of Contents
1. [Semiconducting Equations](#project-title)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Acknowledgments](#acknowledgments)

---

## Project Title: Semiconducting Equations
This python based tool allows for the calculation of common semiconductor equations such as mobility, conductivity, and drift current densities for holes (h+) and electrons (e-). 
This project is the final project for PHYS 4840. 
    
## Description
The Semiconductor Tool uses the equation J = q n mu E to calculate drift current density, mobility, and conductivity. Using spattial and temporal 
grids to integrate the current densities over. These are integrated using the trapezoidal rule. This tool also includes a relative permitivity table.                                          
                                          

## Installation
git clone https://github.com/Kayley-Galbraith/semiconductor_tool.git
cd semiconductor_tool
Dependencies
pip install numpy                                          
                                          
Example: 
git clone https://github.com/Kayley-Galbraith/semiconductor_tool.git
install dependences 
pip install numpy                                         
make/build/install...whatever is needed
set environment variables?
how to launch the program

## Usage
Parameters
    material 
    n0, p0 are the Equilibrium concentrations
    mu_e, mu_h are mobilities
    x and t, spatial and temporal grids
To run the script: 
python semiconductor_tool.py                                          
## Contributing

Contributions are welcome! Please follow these steps:

(1) Fork the repository.

(2) Create a new branch for your feature or bugfix.
                                         
(3) Submit a pull request with a detailed description of your changes.

## License
This project is distributed under the MIT license. 

## Acknowledgments
K Galbraith thanks Dr. Joyce, Eliza Frankel, and Dr. Micah Miller for class instruction. 


