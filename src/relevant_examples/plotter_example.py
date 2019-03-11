from gradient_descent_plotter import  GradientDescentPlotter

gp = GradientDescentPlotter()

def f(x):
    return x[0]**2 + x[1]**2

gp.plotGradientDescent(f,[2,2],100,.001)