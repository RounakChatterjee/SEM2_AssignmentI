import numpy as np
import numpy.linalg as l
'''
This program finds the eigen value of a square matrix using the QR series 
theory
'''
# Decomposition of A into Q and R
A = np.array([[5,-2],[-2,8]],dtype = np.float64)
print(" Q Matrix= \n",l.qr(A)[0],"\n")
print(" R Matrix= \n",l.qr(A)[1],"\n")

'''
We know that continious QR decompisition of the Matrix 
yields the Diagonal form as :
D = (Q1.Q2...QN)^T.A.(Q1.Q2...QN)
'''
def check_diagonal(D):
	error_threshold = 1.0e-8
	for i in range(D.shape[0]):
		for j in range(D.shape[1]):
			if(i!=j):
				if(abs(D[i,j])>=error_threshold): 
					return False
			else:	
				continue
	return True
			
D = A
while(check_diagonal(D) == False):
	Q = l.qr(D)[0]
	D = np.dot(np.transpose(Q),np.dot(D,Q))
print("the Eigen Values are (QR Computed): ")
for i in range(D.shape[0]):
	print(D[i,i])
# This uses the inbuild Numpy function to find the eigen values
print("\nEigen Values (Function calculated):")
print(l.eigvalsh(A))