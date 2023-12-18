import numpy as np
import matplotlib.pyplot as plt
 
 
f = lambda x : x[0] * np.exp(-x[0]**2 - x[1]**2)
 
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 3, 100)
X, Y = np.meshgrid(x, y) # mesh grid matric
Z = f([X, Y]) 
 
# for wireframe, control the wire density by rstride and cstride
fig = plt.figure(figsize=(9, 6))
ax = plt.axes(projection = '3d')
ax.plot_wireframe(X, Y, Z, color ='blue',
    alpha=0.3, rstride = 1, cstride = 1)
ax.set_xlabel('X'), ax.set_ylabel('Y')
ax.set_zlabel('f(X,Y)')
ax.view_init(10, -60)  #(elev=-165, azim=60)
plt.title('Wireframe (Mesh) Plot')
plt.show()