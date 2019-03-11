import numpy as np
from scipy import optimize


class GradientDescent():
    eps = np.sqrt(np.finfo(float).eps)

    def gradient_descent(self, g, x, tol, n):
        counterinner=0
        for i in range(n):
            print(i)
            g1 = g(x)
            z = optimize.approx_fprime(x, g, self.eps)
            z0 = np.linalg.norm(z)

            if (z0 == 0):
                return x, g1,counterinner
            z = z / z0
            del1 = 0
            del3 = 1000
            g3 = g(x - del3 * z)
            while (g3 >= g1):
                counterinner+=1
                del3 = del3 / 2
                g3 = g(x - del3 * z)
                if (del3 < tol / 2):
                    return x, g1,counterinner
            print("Inner loop ran %d times"%counterinner)
            del2 = del3 / 2
            g2 = g(x - del2 * z)
            h1 = (g2 - g1) / del2
            h2 = (g3 - g2) / (del3 - del2)
            h3 = (h2 - h1) / del3
            del0 = .5 * (del2 - h1 / h3)
            g0 = g(x - del0 * z)
            delta = del0
            geval = g0
            if g0 < g3:
                delta = del3
                geval = g3
            x = x - delta * z
            if abs(geval - g1) < tol:
                return x, geval,counterinner



    def gradient_single_step(self,g,x,tol,n):
        g1 = g(x)
        z = optimize.approx_fprime(x, g, self.eps)
        z0 = np.linalg.norm(z)

        if (z0 == 0):
            return x, g1,
        z = z / z0
        del1 = 0
        del3 = 1
        g3 = g(x - del3 * z)
        while (g3 >= g1):
            del3 = del3 / 2
            g3 = g(x - del3 * z)
            if (del3 < tol / 2):
                return x, g1
        del2 = del3 / 2
        g2 = g(x - del2 * z)
        h1 = (g2 - g1) / del2
        h2 = (g3 - g2) / (del3 - del2)
        h3 = (h2 - h1) / del3
        del0 = .5 * (del2 - h1 / h3)
        g0 = g(x - del0 * z)
        delta = del0
        geval = g0
        if g0 < g3:
            delta = del3
            geval = g3
        x = x - delta * z
        return x, geval
