'''
======================
Triangular 3D surfaces
======================

Plot a 3D surface with a triangular mesh.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from gradient_descent import GradientDescent


grad = GradientDescent()

n_radii = 8
n_angles = 36

xguess=[2,2]

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius.
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())* (xguess[0]*1.5)
y = np.append(0, (radii*np.sin(angles)).flatten())* (xguess[1] *1.5)

# Compute z to make the pringle surface.
z = x**2+y**2

print(x)
print(y)

print(z)

plt.ion()
fig = plt.figure()

theta = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
zlist = np.linspace(-2, 2, 1000)
rlist = zlist**2 + 1
xlist = rlist * np.sin(theta)
ylist = rlist * np.cos(theta)




def f(x):
    return x[0]**2 + x[1]**2



for i in range(80,len(z),10):
    plt.clf()  # Clear the figure
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x[:i], y[:i], z[:i], linewidth=0.2, antialiased=True)
    # ax.plot(xlist[:i], ylist[:i], zlist[:i], label='parametric curve')
    #ax.plot(np.zeros(i), np.zeros(i), zlist[:i], label='parametric curve')
    plt.pause(.0005)



for i in range(0,10000):
    ax = fig.gca(projection='3d')
    newxguess = grad.gradient_single_step(f,xguess,.005,100)[0]
    ax.plot([xguess[0]]+ [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)] )
    xguess = newxguess
    plt.pause(.2)



