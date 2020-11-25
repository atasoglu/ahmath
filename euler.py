

def eulerf(f, xi, yi, h, iteration):
    y = [yi] # y = [y0, y1, y2, ..., yn]
    for i in range(1, iteration):
        y.append(yi + f(xi)*h)
        yi = y[i]
        xi += h
    
    return y


def euler(dy, yi, h):
    y = [yi] # y = [y0, y1, y2, ..., yn]
    for i in range(1, len(dy)):
        y.append(yi + dy[i]*h)
        yi = y[i]
    
    return y



import math
import matplotlib.pyplot as plt

step = 0.1
time = 3 # sn
iteration = math.floor(time/step)

g = 9.81 # m/s^2

t = [i * step for i in range(iteration)]
dx2 = [-g for _ in range(iteration)]

# plt.xlabel('zaman-s')
# plt.ylabel('ivme-m/s^2')
# plt.plot(t, dx2, 'r-o', label='ivme')


dx = euler(dx2, yi = 0, h = step)

# plt.xlabel('zaman-s')
# plt.ylabel('hız-m/s')
# plt.plot(t, dx, 'b-^', label='hız')

x = euler(dx, yi = 100, h = step)

# plt.xlabel('zaman-s')
# plt.ylabel('konum-m')
# plt.plot(t, x, 'g-*', label='konum')


x0 = 100
x_ref, v_ref = [], []

h = 0
for i in range(iteration):
    x_ref.append(-0.5 * g * (h**2) + x0)
    v_ref.append(-g * h)
    h += step

fig, (ax0, ax1) = plt.subplots(ncols= 2, figsize=(12, 5))

# Karsilastirma - konum
ax0.grid()
ax0.set_xlabel('zaman-s')
ax0.set_ylabel('konum-m')
ax0.plot(t, x_ref, 'b-^', label='x-analitik')
ax0.plot(t, x, 'r-*', label='x-euler')
ax0.legend()

# Karsilastirma - hız
ax1.grid()
ax1.set_xlabel('zaman-s')
ax1.set_ylabel('hız-m/s')
ax1.plot(t, v_ref, 'b-^', label='v-analitik')
ax1.plot(t, dx, 'r-*', label='v-euler')
ax1.legend()

x_diff, v_diff = [], []

for i in range(iteration):
    x_diff.append(abs(x[i] - x_ref[i]))
    v_diff.append(abs(dx[i] - v_ref[i]))

# plt.plot(x_diff, 'b--', label='x-hata')
# plt.plot(v_diff, 'r-.', label='v-hata')


plt.tight_layout()
# plt.grid()
plt.legend()
plt.show()