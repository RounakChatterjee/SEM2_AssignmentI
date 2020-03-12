'''
This program solves a set of linear equation using the numpy package solve.
'''
import numpy as np
A = np.array([[1.0,0.67,0.33],[0.45,1.0,0.55],[0.67,0.33,1.0]],dtype = np.float64)
b = 2.0*np.ones(3,dtype = np.float64)
sol = np.linalg.solve(A,b)
print("The Solution Vector is = \n",sol)

'''
computing for the problem solved using the fact that we were a two decimal places computer, the error creeped in due to
truncation and hnce the value of the second vector varied from the expected result.


'''
