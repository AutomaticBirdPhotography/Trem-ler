import matplotlib.pyplot as plt
import numpy as np

(fig, ax) = plt.subplots(figsize = (4,4))

def kex(N):
    alpha=2*np.pi/N
    alphas = alpha*np.arange(N)
    coordX = np.cos(alphas)
    coordY = np.sin(alphas)

    return np.c_[coordX, coordY, alphas]

N = 10
r = 1.2
points = kex(N)
ax.scatter(points[:,0], points[:,1])

for i in range(0,N):
    a = points[i,2] 
    x,y = (r*np.cos(a), r*np.sin(a))
    if points[i,0] < 0: a = a - np.pi
    ax.text(x,y, "AAA", rotation = np.rad2deg(a), ha="center", va="center",
                    bbox=dict(facecolor = "none", edgecolor ="red"))

ax.axis("off")

plt.show()