from mpl_toolkits.mplot3d import Axes3D
from gradient_descent import GradientDescent
import matplotlib.pyplot as plt
import numpy as np
class GradientDescentPlotter():

    grad = GradientDescent()


    def get_domain(self, f, domain_bounds):
        n_radii = 8
        n_angles = 36


        # Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
        radii = np.linspace(0.125, 1.0, n_radii)
        angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)

        # Repeat all angles for each radius.
        angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

        # Convert polar (radii, angles) coords to cartesian (x, y) coords.
        # (0, 0) is manually added at this stage,  so there will be no duplicate
        # points in the (x, y) plane.

        xlist = np.append(0, (radii * np.cos(angles)).flatten()) * domain_bounds[0]
        ylist = np.append(0, (radii * np.sin(angles)).flatten()) * domain_bounds[1]

        x = [xlist,ylist]

        # Compute z to make the pringle surface.
        z = f(x)
        return xlist,ylist,z

    def plotGradientDescent(self, f, domain_bounds, xguess,n,tol):

        x,y,z = self.get_domain(f,domain_bounds)

        print(x,y,z)

        plt.ion()
        fig = plt.figure()

        for i in range(10, len(z), 9):
            plt.clf()  # Clear the figure
            ax = fig.gca(projection='3d')
            ax.plot_trisurf(x[:i], y[:i], z[:i], linewidth=0.2, antialiased=True)
            plt.pause(.0005)


        for i in range(0, n):
            ax = fig.gca(projection='3d')
            newxguess = self.grad.gradient_single_step(f, xguess, .005, 100)[0]
            ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)])
            xguess = newxguess
            plt.pause(.2)
        plt.pause(500)