# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import numpy as np
import matplotlib.pyplot as plt

h=0.1
N=5.0/0.1
x=np.zeros(50)
y=np.zeros(50)
z=np.zeros(50)
def dx_dt(x,y,z):
    return(10.0*(y-z))


def dy_dt(x,y,z):
    return(28.0*x-y-x*z)


def dz_dt(x,y,z):
    return(-2.67*z+x*y)


for i in range(len(x)-1):
    x[i+1]=x[i]+h*(dx_dt(x[i],y[i],z[i]))
    y[i+1]=x[i]+h*(dy_dt(x[i],y[i],z[i]))
    z[i+1]=x[i]+h*(dz_dt(x[i],y[i],z[i]))

plt.ply(x,y)
plt.savefig("xy.png")
plt.close()
plt.ply(x,z)
plt.savefig("xz.png")
plt.close()





