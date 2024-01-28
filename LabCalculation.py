import sympy as sp
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr
import numpy as np

sp.init_printing()
#Initiates all variables, where x = µ*, y = µ, b1 = β1, b2 = β2 a = Onsager, and c = (1/4πε0)*(2/a^3)
x, y = sp.symbols('x y', real=True)
a = (8.40*10**(-10))
c = ((1/(4*np.pi*(8.85*10**(-12)))*(2/a**3)))
b1 = (1.50*10**(-19))
b2 = (7.75*10**(-19))
#Sets up our system of equations
eq1 = sp.Eq((c*(x-y)**2), b1)
eq2 = sp.Eq((c*((x**2)-(y**2))), b2)
#Solves system of eqautions for dipole moment values
ans = sp.solve([eq1,eq2],dict=True)
#Outputs in LaTeX form to Jupyter
ans
