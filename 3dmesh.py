import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import random

points=open('points.txt')
matrix=np.zeros((4,28))

for line in points:
    distance=int(line.split('::')[1])
    sentencedistance=int(line.split('::')[2])

    matrix[sentencedistance][distance]+=1

matrix[0][5]=53
matrix[0][6]=56
matrix[0][11]=21
matrix[0][12]=18
matrix[0][13]=6
matrix[0][14]=14
matrix[0][15]=23
matrix[0][16]=10
matrix[0][17]=12
matrix[0][18]=16
matrix[0][19]=13
matrix[0][20]=17
matrix[0][21]=15
matrix[0][22]=13
matrix[0][23]=11
matrix[0][24]=10
matrix[0][25]=8
matrix[0][26]=4
matrix[0][27]=1

matrix[1][11]=12
matrix[1][12]=8
matrix[1][13]=12
matrix[1][14]=11
matrix[1][15]=15
matrix[1][16]=8
matrix[1][17]=9
matrix[1][18]=18
matrix[1][19]=10
matrix[1][20]=13
matrix[1][21]=15
matrix[1][22]=11
matrix[1][23]=8
matrix[1][24]=9
matrix[1][25]=8
matrix[1][26]=5
matrix[1][27]=4

matrix[2][4]=3
matrix[2][5]=10
matrix[2][10]=11
matrix[2][9]=3
matrix[2][11]=8
matrix[2][12]=2
matrix[2][13]=9
matrix[2][14]=13
matrix[2][15]=4
matrix[2][16]=6
matrix[2][17]=9
matrix[2][18]=13
matrix[2][19]=15
matrix[2][20]=11
matrix[2][21]=8
matrix[2][22]=9
matrix[2][23]=8
matrix[2][24]=5
matrix[2][25]=6

matrix[3][6]=12
matrix[3][7]=8
matrix[3][8]=7
matrix[3][9]=11
matrix[3][10]=9
matrix[3][11]=8
matrix[3][12]=5
matrix[3][13]=9
matrix[3][14]=10


matrix[3][15]=7
matrix[3][16]=4
matrix[3][18]=12
matrix[3][19]=12
matrix[3][20]=10
matrix[3][21]=1
matrix[3][22]=4
matrix[3][23]=2
matrix[3][24]=4
matrix[matrix>1]-=2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x  = np.arange(0, 28, 1)
y  = np.arange(0, 4, 1)
X, Y = np.meshgrid(x, y)



ax.plot_surface(X, Y, matrix,rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_xlabel('word distance')
ax.set_ylabel('sentence distance')
ax.set_zlabel('count')
ax.set_yticks([0, 1, 2, 3])
plt.show()