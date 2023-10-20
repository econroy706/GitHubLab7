#!/usr/bin/env python
# coding: utf-8

# In[1]:


def force(t,pos,v, b):
    x2 = -k*(pos-xC) + -b * v
    return (x2)
x0 = 1 ##m
xC = 0 
v0 = 0 ##m/s
m = .1 ##kg
k = 10 ##N/m
g = 9.8
D = 100 ## m
beta = 1.6 * 10**-4 ##Ns/m2
b = D * beta

x0 = 1 ##m
v = 100
v0 = 0 ##m/s
m = .1 ##kg
k = 10 ##N/m
g = 9.8

nsteps = 1000
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t,dt=np.linspace(0,30,nsteps,retstep=True)


print (dt)

data = np.zeros((nsteps, 2))
vel = v0
pos = x0

for i, ti in enumerate(t):
      acc=force(t,pos,vel, b)/m
      vel=vel+acc*dt
      pos=pos+vel*dt
      if(i==0): #reset on first round so i=0 gets x0,v0
            vel=v0
            pos=x0
      data[i]=t[i], pos #fill the data array with our data
print (data)


plt.plot(data[:,0], data[:,1], label = "calc soln")
omega = -(k/m)**.5
time = t
xt = x0*np.cos(omega*t)
##plt.plot(t, xt, label = "Analytical Sol'n")
plt.legend ()
plt.xlabel ("Time")
plt.ylabel ("Amplitude")
plt.title ("Lab 6 GHO damping effect")
plt.savefig("Lab6Figure.png")
plt.close()


# In[ ]:




