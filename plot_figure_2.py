from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

import pickle

with open('recursion_table_5.pickle', 'rb') as handle:
		table = pickle.load(handle)

# fig = plt.figure()
fig = plt.figure(figsize=(12,10))
ax = plt.axes(projection="3d")


x_points = []
y_points = []
z_points = []

M = len(table) 
Q = len(table[0])
for i in range(M):
	for j in range(Q):
		z = table[i][j]
		if (z != -1000) and (z != 0):
			x_points.append(i)
			y_points.append(j)
			z_points.append(table[i][j])

# print 'x', x_points
# print 'y', y_points
# print 'z', z_points 
# #1441aa -- our blue
# #007800 -- our green
# #aa272f -- our red


ax.scatter3D(x_points, y_points, z_points, c='#aa272f', marker ='o');

# ax.set_xlabel('m', fontname = 'Microsoft Sans Serif', fontsize=18)
# ax.set_ylabel('q',fontname = 'Microsoft Sans Serif',fontsize=18)
# ax.set_zlabel('P(m,q)',fontname = 'Microsoft Sans Serif',fontsize=18)
# ax.zaxis.set_tick_params(labelsize=10)
# fig.suptitle('Probability of Smearing under Uniform Distribution', fontsize=16)

plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt



# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x =[1,2,3,4,5,6,7,8,9,10]
# y =[5,6,2,3,13,4,1,2,4,8]
# z =[2,3,3,3,5,7,9,11,9,10]



# ax.scatter(x, y, z, c='r', marker='o')

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()