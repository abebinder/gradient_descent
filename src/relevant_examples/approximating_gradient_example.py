from scipy import optimize
import numpy as np

#define our mltivariable function
def f(x):
    return np.sin(-x[0]*x[1])

#small number
eps = np.sqrt(np.finfo(float).eps)

#find gradient vector at x0=1, x1=1 for function f.
print(optimize.approx_fprime([1,1],f,eps))