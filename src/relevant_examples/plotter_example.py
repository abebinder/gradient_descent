from gradient_descent_plotter import  GradientDescentPlotter

gp = GradientDescentPlotter()

from numpy import sin

def f(x):
    return x[0]**2 + x[1]**2

def g(x):
    return (x[0]**3)-(12*x[1]*x[0])+(8*x[1]**3)

def mike(x):
    return sin(x[0])+x[0]/2 + sin(x[1]) + x[1]/2

def single(x):
    return x[0]**2

gp.plotGradientDescent(mike,[[2,8],[2,8]],[6,7],100,.001,surface_sample=20)
#gp.plotGradientDescent(single,[[0,2]],[6],100,.001,surface_sample=20)