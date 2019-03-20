import time

from mpl_toolkits.mplot3d import Axes3D
from gradient_descent import gradient_single_step,eps
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

print(matplotlib.__version__)

class GradientDescentPlotter():


    def getsquareDomain(self,f,bounds,n):
        xdiff = bounds[0][1] - bounds[0][0]
        ydiff = bounds[1][1] - bounds[1][0]
        xlist = np.arange(bounds[0][0], bounds[0][1], xdiff/n)
        ylist = np.arange(bounds[1][0], bounds[1][1], ydiff/n)
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

        # input("Press Enter to continue...")
        # print("lets go!")
        ax = fig.gca(projection='3d')
        print(f(xguess))
        print(xguess[0])
        print(xguess[1])
        ax.plot([xguess[0]], [xguess[1]], [f(xguess)], marker='o', markersize=5, color="red")
        plt.title('x=%f, y=%f, z=%f' % (xguess[0], xguess[1], f(xguess)), y=1.08)
        plt.draw()
        plt.show(block=False)

        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()



        for i in range(0, 6):
            ax = fig.gca(projection='3d')
            newxguess = gradient_single_step(eps, f, xguess, .005, 100)[0]
            # ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)],'k')
            inneriter = 10
            for j in range(inneriter+1):
                plt.ion()
                betweenx = xguess[0] + (newxguess[0] - xguess[0])* (1/inneriter)*j
                betweeny = xguess[1] + ( newxguess[1] - xguess[1]) * (1/inneriter)*j
                print("x=%f"%betweenx)
                print("y=%f"%betweeny)
                #z= f([betweenx,betweeny])
                z = f(xguess) + (f(newxguess) - f(xguess)) * (1 / inneriter) * j
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
        plt.plot(xguess[0], f(xguess), marker='o', markersize=5, color="red")
        plt.title('x=%f, y=%f' % (xguess[0], f(xguess)), y=1.08)
        plt.draw()
        plt.show(block=False)
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()

        for i in range(0, 6):
            ax = fig.gca()
            newxguess = gradient_single_step(eps, f, xguess, .005, 100)[0]
            # ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)],'k')
            inneriter = 10
            for j in range(inneriter+1):
                plt.ion()
                betweenx = xguess[0] + (newxguess[0] - xguess[0])* (1/inneriter)*j
                y= f([betweenx])
                y= f(xguess) + (f(newxguess) - f(xguess))* (1/inneriter)*j
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