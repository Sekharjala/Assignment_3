#Code by GVV Sharma
#November 19, 2019
#released under GNU GPL
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A = np.array([3,1,-2]).reshape((3,1))
B = np.array([4,0,4]).reshape((3,1))
C = np.array([2,-1,-56]).reshape((3,1))
D = np.array([5,-6,-60]).reshape((3,1))
#Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_CD[0,:],x_CD[1,:],x_CD[2,:],label="CD")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(D[0],D[1],D[2],'o')
ax.text(3,1,-2, "A", color='red')
ax.text(4,0,4, "B", color='red')
ax.text(5,-6,60, "C", color='red')
ax.text(5,-6,-60, "D", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
#if using termux
#else
#plt.show()
