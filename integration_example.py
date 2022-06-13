import math
import matplotlib.pyplot as plt

def midpoint_rule(func, a, b, n):
    """
    Parameters
    ----------
    func : a lambda function for the integrand
    a : the lower bound
    b : the upper bound
    n : number of segments used in the integration

    Returns
    -------
    I : the evaluated integral
    """
    
    dx = (b-a)/n
    
    curr_lower = a
    curr_upper = a+dx
    
    I = 0
    
    for _ in range(n):
        I_curr = func((curr_lower+curr_upper)/2)*dx
        I = I + I_curr
        curr_lower = curr_lower + dx
        curr_upper = curr_upper + dx
    
    print(I)
    return(I)

def simpsons_rule(func, a, b, n):
    """
    Parameters
    ----------
    func : a lambda function for the integrand
    a : the lower bound
    b : the upper bound
    n : number of segments used in the integration

    Returns
    -------
    I : the evaluated integral
    """
    
    dx = (b-a)/n
    
    curr_lower = a
    curr_upper = a+dx
    
    I = 0
    
    for _ in range(n):
        I_curr = (func(curr_lower) + 4*func((curr_lower+curr_upper)/2) + \
            func(curr_upper))*dx/6
        I = I + I_curr
        curr_lower = curr_lower + dx
        curr_upper = curr_upper + dx
    
    print(I)
    return(I)

f = lambda x: math.sin(x)
a = 0
b = math.pi/2


err_simpsons = []
err_midpoint = []
numiters = 9

for expo in range(numiters):
    err_simpsons.append(abs(simpsons_rule(f, a, b, 2**expo)-1))
    err_midpoint.append(abs(midpoint_rule(f, a, b, 2**expo)-1))

print(err_simpsons, err_midpoint)

convergence_simpsons = -math.log(err_simpsons[-1]/err_simpsons[0],2) / \
    math.log((2**(numiters-1))/2**0,2)
convergence_midpoint = -math.log(err_midpoint[-1]/err_midpoint[0],2) / \
    math.log((2**(numiters-1))/2**0,2)


x_axis = [i for i in range(numiters)]
plt.plot(x_axis, err_simpsons)
plt.plot(x_axis, err_midpoint)
plt.legend(["simpsons convergence rate: % s" % convergence_simpsons, \
            "midpoint convergence rate: % s" % convergence_midpoint])
plt.yscale("log")
plt.show