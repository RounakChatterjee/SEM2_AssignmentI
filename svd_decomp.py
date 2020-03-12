''''
The svd method is a way to convert an (m x n) rectangular matrix to 
an equivalent form that is almost a diagonal form
 to Achieve this we use the tasformation

 S = U^T.A.V, where U and V are (m x m) and (n x n) orthogonal 
 matrices respectively.
 If we choose the matrix A^T.A , we'll find it to be symmetric and can be 
 eigen value decomposed using any standard method where 
 A^T.A will be diagonalized by V, while similarly A.A^T will be
 diagonalized U.
 '''
import numpy as np
import numpy.linalg as l
import timeit as t

A = np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]],dtype = np.float64)
ATA = np.dot(np.transpose(A),A)
AAT = np.dot(A,np.transpose(A))

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

'''
Transformer Finds the corresponding Diagonalizing matrices by QR itteration.
'''
def transformer(D):
	S = np.identity(D.shape[0],dtype = np.float64)
	while(check_diagonal(D) == False):
		Q = l.qr(D)[0]
		S = np.dot(S,Q)
		D = np.dot(np.transpose(Q),np.dot(D,Q))
	return S

V = transformer(ATA)
U = transformer(AAT)
#We obtain SVD by direct transformation formula
S = np.dot(np.transpose(U),np.dot(A,V))
for i in range(S.shape[0]):
	for j in range(S.shape[1]):
		if(abs(S[i,j])<=1.0e-6):
			S[i,j] = 0.0
print("SVD Matrix by direct computation:\n",S,"\n")
print("Time Taken = ",t.timeit(),"\n")
print("SVD Diagonal elements by function:\n",l.svd(A)[1],"\n")
print("Time Taken = ",t.timeit())

'''
The SVD Values obtained via direct theoretical calculation and using 
package differ due to the fact that the SVD values are square roots of the
eigenvalues of A^T.A or A.A^T, so there is a particular freedom to choose
the particular sign.

Since we used the method to find the transformer so it might yield a negative,
The functional Module uses the method to find Eigen Values  and by convention made positive. 
'''