def runge_kutta(f, xi, yi, h, iteration):

    y = [yi] # y = [y0, y1, y2, ... , yn]

    for i in range(1, iteration):
        k1 = h * f(xi, yi)
        k2 = h * f(xi + 0.5*h, yi + 0.5*k1)
        k3 = h * f(xi + 0.5*h, yi + 0.5*k2)
        k4 = h * f(xi + h, yi + k3)

        y = y + [yi + (k1 + 2*k2 + 2*k3 + k4)/6]

        xi += h
        yi = y[-1]

    return y

import math
import matplotlib.pyplot as plt

step = 0.01
interval = 3
ITER = math.floor(interval/step)
x0 = 0
y0 = 1

def f(x):
    return math.exp((x**2)/2)

def dydx(x, y):
    return x*y

x = [i*step for i in range(ITER)]
y = [f(xi) for xi in x]

y_rk = runge_kutta(dydx, x0, y0, step, ITER)

plt.plot(x, y, 'g', marker = 'o', label = 'y')
plt.plot(x, y_rk, 'b', marker = 'v', label = 'y (runge-kutta)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('runge-kutta method') 
plt.legend()
plt.show()

err = []
for i in range(ITER):
    err = err + [abs(y[i] - y_rk[i])]

plt.plot(err, 'r')

plt.xlabel('iteration')
plt.ylabel('error')
plt.title('error, h: ' + str(step) + ', iteration: ' + str(ITER)) 
plt.show()
