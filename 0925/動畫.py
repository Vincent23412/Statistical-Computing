import numpy as np
import matplotlib.pyplot as plt

n = 20 # n terms as n goes to infinity
f = np.arange(n)
x = np.linspace(-3*np.pi, 3*np.pi,200)
y = 0 #np.zeros(len(x)) # initial setting
plt.axis([-3*np.pi, 3*np.pi, -3, 3]) # fix axis range
plt.grid(True)
for i in f:  
    k = 2*i+1
    y = y + np.sin(k*x) / k
    plt.cla()
    plt.plot(x, y*4/np.pi, color='b')
    plt.pause(0.5) # not work for jupyter

# plt.title('Squared wave')
plt.show()