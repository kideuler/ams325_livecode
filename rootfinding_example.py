import math
import numpy as np
import matplotlib.pyplot as plt

def secant(f, a, b, tol):
    iters = 0
    x_k = (a+b)/2
    x_k1 = b
    while abs(x_k-x_k1) > tol:
        p = x_k
        x_k = x_k - f(x_k)*(x_k - x_k1)/(f(x_k)- f(x_k1))
        x_k1 = p
        iters = iters+1    
    return x_k, iters

def newtons(f, f_prime, a, b, tol):
    iters = 0
    x_k = (a+b)/2
    x_k1 = 0
    while abs(x_k-x_k1) > tol:
        x_k1 = x_k
        x_k = x_k - f(x_k)/f_prime(x_k)
        iters = iters+1    
    return x_k, iters


def bisection(f, a, b, tol):
    iters = 0
    while (b-a) > tol:
        m = a + (b-a)/2
        iters = iters + 1
        if np.sign(f(a)) == np.sign(f(m)):
            a = m
        else:
            b = m   
    return (a+b)/2, iters

f = lambda x: math.sin(x)
f_p = lambda x: math.cos(x)
lower = math.pi/2
upper = 5*math.pi/4

print(secant(f, lower, upper, 1e-10))

tols = [10**-expo for expo in range(1,16)]
iters_bisection = [0 for _ in range(15)]
iters_newton = [0 for _ in range(15)]
iters_secant = [0 for _ in range(15)]

for i in range(15):
    pi_bi, iters_bisection[i] = bisection(f, lower, upper, tols[i])
    pi_n, iters_newton[i] = newtons(f, f_p, lower, upper, tols[i])
    pi_sec, iters_secant[i] = secant(f, lower, upper, tols[i])

plt.plot(tols, iters_bisection)
plt.plot(tols, iters_newton)
plt.plot(tols, iters_secant)
plt.legend(["bisection method", "newtons method", "secant method"])

plt.xscale("log")
plt.gca().invert_xaxis()
plt.title("Rootfinding of " +"$\sin(x)$" )
plt.xlabel('error')
plt.ylabel('number of iterations')
plt.show


