import sympy as sp
from sympy.solvers import solve
from sympy.parsing.sympy_parser import parse_expr
import numpy as np

sp.init_printing()

x, y = sp.symbols('x y', real=True)
a = (8.40*10**(-10))
c = ((1/(4*np.pi*(8.85*10**(-12)))*(2/a**3)))
b1 = (1.50*10**(-19))
b2 = (7.75*10**(-19))

eq1 = sp.Eq((c*(x-y)**2), b1)
eq2 = sp.Eq((c*((x**2)-(y**2))), b2)

ans = sp.solve([eq1,eq2],dict=True)

ans
