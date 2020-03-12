'''
This Program uses Conjugate Gradient method to solve for the equation. 
This method finds the Conjugate vectors one by one and finds the solution upto some
arbitary precision.

The Program follows the Algorithm stirctly as depicted in Bulirsch and Stoer 
'''
import numpy as np
#The Matrix equation Ax = b
A= np.array([[0.2,0.1,1.0,1.0,0.0],[0.1,4.0,-1.0,1.0,-1.0],[1.0,-1.0,60.0,0.0,-2.0],[1.0,1.0,0.0,8.0,4.0],[0.0,-1.0,-2.0,4.0,700.0]],dtype = 'double')
b = np.array([1.0,2.0,3.0,4.0,5.0],dtype = 'double')

#This Module checks for the accuracy wrt true solution
x_original = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163],dtype = 'double')
def check_accuracy(x):
	for i in range(len(x)):
		if(np.abs(x[i]-x_original[i])>0.01):
			return False
	return True

#initial Guess vector x0
x0 = np.zeros(5,dtype = 'double')
 #This function finds the solution vector x starting from initial guess
def Con_Grad(A,b,x0):
 	r_old = b-np.dot(A,x0)# Residual vector
 	r_new = np.zeros(5,dtype = 'double')

 	p = r_old#the conjugate vector
 	a = 0.0# Factor used to find next residual vector
 	b = 0.0# Factor used to find next Conjugate vector
 	Ap = np.zeros(5,dtype='double')
 	x = x0
 	'''
 	As the theory Suggests p is actually one of the conjugate vectors in whose 
 	Basis we can find the solution vector
 	So atmost we need runs = the length of the solution vector to find the 
 	complete solution
 	'''
 	for i in range(len(x0)):
 		Ap=np.dot(A,p)
 		a = np.dot(np.transpose(r_old),r_old)/(np.dot(np.transpose(p),Ap))
 		x = x + np.dot(a,p)
 		if(check_accuracy(x) == True):
 			return [x,i]
 		r_new = r_old - np.dot(a,Ap)
 		b = np.dot(np.transpose(r_new),r_new)/(np.dot(np.transpose(r_old),r_old))
 		p = r_new + np.dot(b,p)
 		r_old = r_new
 	return[x,i]
sol = Con_Grad(A,b,x0)
print("solution is\n",sol[0])
print("itterations = ",sol[1])


