import time

from mpl_toolkits.mplot3d import Axes3D
from gradient_descent import gradient_single_step,eps
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

class GradientDescentPlotter():


    def getsquareDomain(self,f,bounds,n):

        domain=[]
        for e in bounds:
            diff = e[1]-e[0]
            domain.append(np.arange(e[0],e[1],diff/n))
        if len(bounds)==2:
            domain[0],domain[1]=np.meshgrid(domain[0],domain[1])
        domain.append(f(domain))
        return tuple(domain)


    def plotGradientDescent(self, f, domain_bounds, xguess,n,tol, surface_sample=100):

        domain = self.getsquareDomain(f,domain_bounds,surface_sample)
        fig = plt.figure()
        plt.draw()
        plt.show(block=False)
        self.waitForKeybordPress()
        self.animatePlotRender(domain, fig)


        self.waitForKeybordPress()
        ax = fig.gca()
        if(len(xguess)==2):
            ax = fig.gca(projection='3d')
        wrappedx = []
        for e in xguess:
            wrappedx.append([e])
        ax.plot(*wrappedx, [f(xguess)], marker='o', markersize=5, color="red")
        plt.title(str((xguess,f(xguess))), y=1.08)
        plt.draw()
        plt.show(block=False)

        self.waitForKeybordPress()



        for i in range(0, 6):
            newxguess = gradient_single_step(eps, f, xguess, .005, 100)[0]
            # ax.plot([xguess[0]] + [newxguess[0]], [xguess[1]] + [newxguess[1]], [f(xguess)] + [f(newxguess)],'k')
            inneriter = 10
            for j in range(inneriter+1):
                plt.ion()
                between = []
                for k in range(len(xguess)):
                    indiv = xguess[k] + (newxguess[k] - xguess[k])* (1/inneriter)*j
                    between.append([xguess[k]] + [indiv])

                z = f(xguess) + (f(newxguess) - f(xguess)) * (1 / inneriter) * j
                between.append([f(xguess)] + [z])
                ax.plot(*between, 'k')
                # plt.title('x=%f, y=%f, z=%f'%(betweenx,betweeny,z),y=1.08)
                plt.pause(.001)

            xguess = newxguess
            plt.draw()
            plt.show(block=False)
            keyboardClick = False
            while keyboardClick != True:
                keyboardClick = plt.waitforbuttonpress()
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
            self.waitForKeybordPress()
        plt.ioff()
        plt.show()

    def getsquareDomain2D(self,f,bounds,n):
        xlist=np.arange(bounds[0][0], bounds[0][1], (bounds[0][1]-bounds[0][0])/n)
        y = f([xlist])
        return xlist, y


    def waitForKeybordPress(self):
        keyboardClick = False
        while keyboardClick != True:
            keyboardClick = plt.waitforbuttonpress()

    def animatePlotRender(self,x,fig):
        increment = int (len(x[0])/20)
        plt.ion()
        for i in range(1, len(x[0]), increment):
            plt.clf()  # Clear the figure
            newx =[]
            if(len(x)==3):
                ax = fig.gca(projection='3d')
                for e in x:
                    newx.append(e[:i])
                ax.plot_surface(*newx, linewidth=0.2, antialiased=True)
            else:
                ax = fig.gca()
                for e in x:
                    newx.append(e[:i])
                ax.plot(*newx)
            plt.pause(.0005)
        plt.ioff()
        plt.show(block=False)

