'''
This method tries to estimate the largest eigen value by taking a trail 
vector and sucsessivley itterating on it to obtain the eigen value.
we stop when the method converges to some particular threshold.

The theory to this is

b(k+1) = A.b(k)/norm(A.b(k))

where b(0) is the initial guess vector

and the eigen value E(k) = b(k)^T.A.b(K)/(b(k)^T.b(k))

for a complex matrix the operations must be conjugate transpose
'''
import numpy as np
A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]],dtype = 'double')

#Initial Guess vector
b0 = np.array([1.0,1.0,1.0]) 
err_thr = 0.01 #1% error
e_val = 0.0#Stores Eigen value
prev_e_val = np.dot(np.transpose(b0),np.dot(A,b0))/np.dot(np.transpose(b0),b0)
b = b0 # stores eigen vector
while(True):
	Ab = np.dot(A,b)
	b = Ab/np.sqrt(np.dot(np.transpose(Ab),Ab))
	e_val = np.dot(np.transpose(b),Ab)/np.dot(np.transpose(b),b)
	if(abs(e_val-prev_e_val)<=err_thr):
		break
	else:
		prev_e_val = e_val
print("The Dominant Eigen Value is:",e_val)
print("The Corresponding Eigen vector is:\n",b)


	
