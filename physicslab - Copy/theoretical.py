import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

total_time = 300
number_of_steps = 40000
GRAVITY = 9.80665
SPRING_CONSTANT = 10.02
MASS = 0.05
X0 = 0.28

def mass_on_spring(y, t, c):
  x, dx = y
  dydt = [dx, -SPRING_CONSTANT/MASS*(x-X0) - GRAVITY - np.sign(dx)*c*dx**2]
  return dydt

c = 0.623
y0 = [0.18, 0]
t = np.linspace(0, total_time, number_of_steps)
sol = odeint(mass_on_spring, y0, t, args=(c,))
x = sol[:, 0]
dx = sol[:, 1]

mass = MASS
gravity = GRAVITY
spring_constant = SPRING_CONSTANT
x0 = X0

# me = MASS*GRAVITY*x + 0.5*SPRING_CONSTANT*(x-X0)**2 + 0.5*MASS*dx**2
me = mass*gravity*x + 0.5*spring_constant*(x-x0)**2 + 0.5*mass*dx**2

dme = np.diff(me)*number_of_steps/total_time

plt.title('Mass on Spring')
# plt.plot(t, x, 'o', label='data', markersize=2)
plt.plot(t[1:], dme, 'o', label='data', markersize=2)
plt.xlabel('Time (s)')
plt.ylabel('Mechanical Energy (J)')

plt.show()