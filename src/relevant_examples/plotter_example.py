from gradient_descent_plotter import  GradientDescentPlotter

gp = GradientDescentPlotter()

def f(x):
    return x[0]**2 + x[1]**2

def g(x):
    return (x[0]**3)-(12*x[1]*x[0])+(8*x[1]**3)

gp.plotGradientDescent(f,[3,3],[2,2],100,.001)