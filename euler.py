def euler(dy, yi, h):

	y = [] # y = [y0, y1, y2, ... , yn]

	for dyi in dy:
		y = y + [yi + dyi * h]
		yi = y[-1]

	return y

def euler_f(f, xi, yi, h, iteration): # alternative

	y = [] # y = [y0, y1, y2, ... , yn]

	for i in range(iteration):
		y = y + [yi + f(xi) * h]
		yi = y[-1]
		xi += h
	
	return y

import math
import matplotlib.pyplot as plt

step = 0.01
time = 3 # sn
iteration = math.floor(time / step)

g = 9.81 # m/s^2

t = [i * step for i in range(iteration)]
dx2 = [-g for i in range(iteration)]
"""
plt.plot(t, dx2, 'r', label = 'ivme')

plt.xlabel('zaman (sn)')
plt.ylabel('ivme (m/s^2)')
"""
dx = euler(dy = dx2, yi = 0, h = step)
"""
plt.plot(t, dx, 'b', label = 'hız')

plt.xlabel('zaman (sn)')
plt.ylabel('hız (m/s)')
"""
x = euler (dy = dx, yi = 100, h = step)
"""
plt.plot(t, x, 'g', label = 'konum')

plt.xlabel('zaman (sn)')
plt.ylabel('konum (m)')
"""
# v0 = 0
x0 = 100
x_ref = []
v_ref = []

h = 0
for i in range(iteration):
	x_ref = x_ref + [-0.5 * g * (h**2) + x0]
	v_ref = v_ref + [-g * h] 
	h += step

x_diff = []
v_diff = []

for i in range(iteration):
	x_diff = x_diff + [abs(x[i] - x_ref[i])]
	v_diff = v_diff + [abs(dx[i] - v_ref[i])]


plt.plot(x_diff, 'b', linestyle = 'dashed', label = 'x-hata')
plt.plot(v_diff, 'r', linestyle = 'dashdot', label = 'v-hata')

plt.xlabel('iterasyon')
plt.ylabel('hata')
plt.legend()
plt.show()
