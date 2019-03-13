import time

from mpl_toolkits.mplot3d import Axes3D
from gradient_descent import GradientDescent
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

print(matplotlib.__version__)

class GradientDescentPlotter():

    grad = GradientDescent()


    def get_domain(self, f, domain_bounds):
        n_radii = 8
        n_angles = 50


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


    def getsquareDomain(self,f,bounds,n):
        xlist=[]
        ylist =[]
        xdiff = bounds[0][1] - bounds[0][0]
        ydiff = bounds[1][1] - bounds[1][0]
        for i in range(n):
            xlist.append(bounds[0][0]+ xdiff* (i/n))
        for i in range(n):
            ylist.append(bounds[1][0] + ydiff * (i / n))
        # Compute z to make the pringle surface.
        xlist = np.array(xlist)
        ylist = np.array(ylist)

        X,Y = np.meshgrid(xlist,ylist)

        Z = f([X, Y])

        return X, Y, Z


    def plotGradientDescent(self, f, domain_bounds, xguess,n,tol, surface_sample=100):

        x,y,z = self.getsquareDomain(f,domain_bounds,surface_sample)

        print(x,y,z)
        print(len(x))
        print(len(y))
        print(len(z))

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        increment = int (len(z)/20)

        plt.draw()
        plt.show(block=False)
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()
        plt.ion()

        for i in range(1, len(z), increment):
            plt.clf()  # Clear the figure
            ax = fig.gca(projection='3d')
            ax.plot_surface(x[:i], y[:i], z[:i], linewidth=0.2, antialiased=True)
            plt.pause(.0005)

        plt.ioff()
        plt.show(block=False)
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()
        # input("Press Enter to continue...")
        # print("lets go!")

        for i in range(0, 6):
            ax = fig.gca(projection='3d')
            newxguess = self.grad.gradient_single_step(f, xguess, .005, 100)[0]
            # ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)],'k')
            inneriter = 10
            for j in range(inneriter+1):
                plt.ion()
                betweenx = xguess[0] + (newxguess[0] - xguess[0])* (1/inneriter)*j
                betweeny = xguess[1] + ( newxguess[1] - xguess[1]) * (1/inneriter)*j
                print("x=%f"%betweenx)
                print("y=%f"%betweeny)
                z= f([betweenx,betweeny])
                ax.plot([xguess[0]] + [betweenx], [xguess[1]] + [betweeny], [f(xguess)] + [z], 'k')
                plt.title('x=%f, y=%f, z=%f'%(betweenx,betweeny,z),y=1.08)
                plt.pause(.001)

            xguess = newxguess
            plt.draw()
            plt.show(block=False)
            keyboardClick = False
            while keyboardClick != True:
                keyboardClick = plt.waitforbuttonpress()
            print(xguess)
            print(f(xguess))
        plt.ioff()
        plt.show()














    def plotGradientDescentTwoD(self, f, domain_bounds, xguess,n,tol, surface_sample=100):

        x,y = self.getsquareDomain2D(f,domain_bounds,surface_sample)

        print(len(x))
        print(len(y))

        fig = plt.figure()


        plt.draw()
        plt.show(block=False)
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()
        plt.ion()

        increment = int (len(y)/20)
        for i in range(1, len(y)+1, increment):
            plt.clf()  # Clear the figure
            ax = fig.gca()
            ax.plot(x[:i], y[:i])
            plt.pause(.0005)

        plt.ioff()
        plt.show(block=False)
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()
        # input("Press Enter to continue...")
        # print("lets go!")

        for i in range(0, 6):
            ax = fig.gca()
            newxguess = self.grad.gradient_single_step(f, xguess, .005, 100)[0]
            # ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)],'k')
            inneriter = 10
            for j in range(inneriter+1):
                plt.ion()
                betweenx = xguess[0] + (newxguess[0] - xguess[0])* (1/inneriter)*j
                y= f([betweenx])
                ax.plot([xguess[0]] + [betweenx], [f(xguess)] + [y], 'k')
                plt.title('x=%f, y=%f'%(betweenx,y),y=1.08)
                plt.pause(.001)

            xguess = newxguess
            plt.draw()
            plt.show(block=False)
            keyboardClick = False
            while keyboardClick != True:
                keyboardClick = plt.waitforbuttonpress()
            print(xguess)
            print(f(xguess))
        plt.ioff()
        plt.show()

    def getsquareDomain2D(self,f,bounds,n):
        xlist=[]
        xdiff = bounds[0][1] - bounds[0][0]
        for i in range(n):
            xlist.append(bounds[0][0]+ xdiff* (i/n))
        # Compute z to make the pringle surface.
        xlist = np.array(xlist)

        y = f([xlist])

        return xlist, y