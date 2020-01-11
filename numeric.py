"""
numeric.py
contains:
* euler -> Euler method
* rk2 	-> Runge-Kutta 2nd order method
* rk4 	-> Runge-Kutta 4th order method
all paramaters are same.
params: (function(x, y), x0, y0, step_size, iteration)
"""
from basic import *

def rk2(func, xi, yi, h, Iter):
    y = [yi]
    for i in range(1, Iter):
        k1 = h * func(xi, yi)
        k2 = h * func(xi + h, yi + k1)
        y.append(yi + 0.5*(k1 + k2))
        xi += h
        yi = y[-1]
    return y

def rk4(func, xi, yi, h, Iter):
    y = [yi]
    for i in range(1, Iter):
        k1 = h * func(xi, yi)
        k2 = h * func(xi + h/2.0, yi + k1/2.0)
        k3 = h * func(xi + h/2.0, yi + k2/2.0)
        k4 = h * func(xi + h, yi + k3)
        y.append(yi + (k1 + 2*k2 + 2*k3 + k4)/6.0)
        xi += h
        yi = y[-1]
    return y    

def euler(func, xi, yi, h, Iter):
    y = [yi]
    for i in range(1, Iter):
        y.append(yi + func(xi, yi)*h)
        xi += h
        yi = y[-1]
    return y
