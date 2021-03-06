from gradient_descent import GradientDescent


def ff(x, y, z):
    return 1/1000 * ((x-2)**2 + (y-5)**2 + (z+3)**2)


def f(x):
    return ff(*x)

g = GradientDescent()

something = g.gradient_descent(f,[1000, 1000, 1000],.00001,5000)

print(something)