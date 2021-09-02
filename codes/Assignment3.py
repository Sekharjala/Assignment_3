#Code by GVV Sharma
#December 7, 2019
#Revised July 15, 2020
#released under GNU GPL
#Functions related to conics

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from conics import *
from params import *

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#if using termux
import subprocess
import shlex
#end if

r=2
O = np.array([0,0])
A = np.array([2,0])
B=  np.array([np.sqrt(3),1])
#Generating all lines
x_OA = line_gen(O,A)
x_OB = line_gen(O,B)
x_circ = circ_gen(O,r)
#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:],label='$OA$')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.05), O[1] * (1 - 0.1) , 'O')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1), A[1] * (1) , 'A')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(O[0], O[1], 'o')
#plt.text(A[0] * (1 + 0.05), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1), B[1] * (1) , 'B')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
len = 200
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = np.sqrt(4)*np.cos(theta)
x_circ[1,:] = np.sqrt(4)*np.sin(theta)
x_circ = (x_circ.T + O).T

#plt.fill_between([0,np.sqrt(3),2],[0,np.sqrt(1),0],color = 'black')
#plt.fill_between(x_points,y_points,color = 'black')

plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

#if using termux
#plt.savefig('./figs/tri_sss.pdf')
#plt.savefig('./figs/tri_sss.png')
#subprocess.run(shlex.split("termux-open ./figs/tri_sss.pdf"))
#else
plt.show()
