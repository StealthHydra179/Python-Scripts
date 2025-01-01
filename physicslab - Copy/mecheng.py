import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from lmfit import minimize, Parameters, report_fit
from scipy.integrate import odeint
import pandas as pd

data = pd.read_csv('run1processed2.csv', header=None)
GRAVITY = 9.80665
NUMBER_OF_STEPS = 40000
TOTAL_TIME = 300
TIME = np.array(data[0], dtype=float)-1.95
X = np.array(data[1], dtype=float)
DX = np.array(data[2], dtype=float)
def f(y, t, params):
  x, dx = y
  try:
    k = params['k'].value
    x0 = params['x0'].value
    c1 = params['c1'].value
    c2 = params['c2'].value
    mass = params['mass'].value
  except KeyError:
    k, x0, c1, c2, mass = params
  return [dx, -k/mass*(x-x0) - GRAVITY - dx*(c1*np.abs(dx)+c2)]
def residual(params, t, x, dx):
  model = odeint(f, [X[0], DX[0]], t, args=(params,))
  me = params['mass']*GRAVITY*model[:, 0] + 0.5*params['k']*(model[:, 0]-params['x0'])**2 + 0.5*params['mass']*model[:, 1]**2
  measured_me = params['mass']*GRAVITY*x + 0.5*params['k']*(x-params['x0'])**2 + 0.5*params['mass']*dx**2
  return (me - measured_me).ravel()

params = Parameters()
params.add('k', value=10, vary=False)
params.add('x0', value=0.328, vary=False)
params.add('c1', value=0.3, vary=True)
params.add('c2', value=0.003, vary=True)
params.add('mass', value=0.09, vary=False)

result = minimize(residual, params, args=(TIME, X, DX))
fitted_data = odeint(f, [X[0], DX[0]], np.linspace(0, TOTAL_TIME, NUMBER_OF_STEPS), args=(result.params,))
me = result.params['mass']*GRAVITY*X + 0.5*result.params['k']*(X-result.params['x0'])**2 + 0.5*result.params['mass']*DX**2
fitted_me = result.params['mass']*GRAVITY*fitted_data[:, 0] + 0.5*result.params['k']*(fitted_data[:, 0]-result.params['x0'])**2 + 0.5*result.params['mass']*fitted_data[:, 1]**2
report_fit(result)
plt.title('Mass on Spring')
plt.plot(TIME, me, 'o', markersize=1)
plt.plot(np.linspace(0, TOTAL_TIME, NUMBER_OF_STEPS), fitted_me, 'r', markersize=1)
plt.xlabel('Time (s)')
plt.ylabel('Mechanical Energy (J)')
plt.show()