import numpy as np
import math
import matplotlib.pyplot as plt

def Solve(A,b):
    if np.size(A,0) == np.size(A,1):
        x = np.linalg.solve(A,b)
    else:
        x = np.linalg.lstsq(A,b,rcond = None)[0]
    return(x)


def Vandermode(xs, degree):
    # assertion of 2D
    assert np.size(xs,1) == 2
    
    # number of points in xs
    npoints = np.size(xs,0)
    
    V = np.zeros((npoints, degree+1),dtype = 'float')
    rhs = np.zeros((npoints,1),dtype = 'float')
    
    for deg in range(degree+1):
        V[:,deg] = xs[:,0]**deg
    rhs[:,0] = xs[:,1]
    
    coeffs = Solve(V,rhs)
    return(coeffs)
    
def Interp(func, xlim, npoints, degree):
    x = np.linspace(xlim[0], xlim[1], npoints, endpoint = True)
    y = func(x)
    xs = np.array([x,y]).T
    
    coeffs = Vandermode(xs,degree)
    Poly = lambda x: sum([coeffs[i]*x**i for i in range(degree+1)])
    return(Poly)



npoints = 31
degree = 30
func = lambda x: x*np.sin(x) + np.cos(x)
xlim = [0, 6*math.pi]

x = np.linspace(xlim[0], xlim[1], npoints, endpoint = True)
y = func(x)
plt.scatter(x,y)

Polynomial = Interp(func, xlim, npoints, degree)

x_axis = np.linspace(xlim[0], xlim[1], 100, endpoint = True)
plt.plot(x_axis,Polynomial(x_axis))