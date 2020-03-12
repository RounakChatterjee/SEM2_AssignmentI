'''
in this program we use the itteration scheme as Showcased in 
Bulirsch and Stoer 

It says that unlike Gauss Siedel where we don't use the ith value of vector x for the kth itteration 
to compute ith value of x for (k+1)th itteration. In relatiation method we use the fact that 

value of ith component of x for (k+1) th itteration = 
(1-omega)*value of ith component of x for kth itteration + omega*u

where u = value of ith component of x for (k+1)th itteration computed by gauss siedel method
'''
import numpy as np
#Input Values 
A= np.array([[0.2,0.1,1.0,1.0,0.0],[0.1,4.0,-1.0,1.0,-1.0],[1.0,-1.0,60.0,0.0,-2.0],[1.0,1.0,0.0,8.0,4.0],[0.0,-1.0,-2.0,4.0,700.0]],dtype = 'double')
b = np.array([1.0,2.0,3.0,4.0,5.0],dtype = 'double')
# For Tolerance Testing 
x_original = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163],dtype = 'double')
'''
This Function does the actual calculation for one itteration
'''
def next_itteration_value(x_prev,omega):
	x = np.zeros(len(x_prev),dtype = 'double')
	for i in range(len(x_prev)):
		for j in range(A.shape[1]):
			if(j<i):
				x[i] = x[i]+(A[i,j]/A[i,i]*x[j])
			elif(j>i):
				x[i] = x[i]+(A[i,j]/A[i,i]*x_prev[j])
			else: 
				x[i] = x[i] + x_prev[i]
		x[i] = (b[i]/A[i,i] - x[i])*omega + x_prev[i]	
	return x
#This functions tests accuracy to 0.01 
def check_accuracy(x):
	for i in range(len(x)):
		if(np.abs(x[i]-x_original[i])>0.01):
			return False
	return True

#section finds and prints the solution.
x = np.zeros(5,dtype = 'double')
c = 0
while(check_accuracy(x) == False):
	c = c+1
	x = next_itteration_value(x,1.25)
print("Solution vector for omega = 1.25 = \n",x)
print("Itterations = ",c)

'''
To illustrate the power of this method we tweaked the value of omega 
and found a rather fast convergence for omega = 1.283 which we depict here

'''
x = np.zeros(5,dtype = 'double')
c = 0
while(check_accuracy(x) == False):
	c = c+1
	x = next_itteration_value(x,1.283)
print("Solution vector for omega = 1.283 = \n",x)
print("Itterations = ",c)