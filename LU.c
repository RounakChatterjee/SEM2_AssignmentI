/*
This Program uses The GSL linear algebra function to LU Decompose the given Matrix
The Program structure consists of a function that displays the Matrix in matrix form while another function 
does simple Matrix Multiplication
The main function does the LU decomposition and illustrates that it is indeed correct by finding the Product of the Matrices.
*/
#include <stdio.h>
#include <gsl/gsl_linalg.h>

void show(gsl_matrix *A,int n)//This Function Displays a Matrix in readable form
{
  for(int i = 0;i<n;i++)
  {
    for(int j=0;j<n;j++)
    {
      printf("%0.3f\t",gsl_matrix_get(A,i,j));
    }
    printf("\n");
  }
}

 gsl_matrix* mat_mul(gsl_matrix *A,gsl_matrix *B,int n)//This function Multiplies two matrices returning it to another matrix
{
 gsl_matrix* C;
 C = gsl_matrix_alloc(3,3);
 double sum = 0.0;
for(int i = 0;i<n;i++)
  {
    for(int j=0;j<n;j++)
    {
      for(int k=0;k<n;k++)
       {sum = sum+ (gsl_matrix_get(A,i,k)*gsl_matrix_get(B,k,j));}
     gsl_matrix_set(C,i,j,sum);
     sum = 0.0;
    }
  }
  return C;
}


int main (void)//This is the Main Program that does the LU decomposition and verifies it
{
  double a_data[] = {1,0.67,0.33,0.45,1.0,0.55,0.67,0.33,1.0}; // row wise stored data
  gsl_matrix *A;
  gsl_matrix *A_copy;
  gsl_matrix *L;
  gsl_matrix *U;
  gsl_matrix *Prod;
  int s;
  gsl_permutation * p = gsl_permutation_alloc (3);
  A = gsl_matrix_alloc(3,3);
  A_copy = gsl_matrix_alloc(3,3);
  L = gsl_matrix_alloc(3,3);
  gsl_matrix_set_all(L,0.0);//stores L matrix
  U = gsl_matrix_alloc(3,3);
  gsl_matrix_set_all(U,0.0);// stores U matrix

  //Allocation of data to the A matrix
  int k = 0;
  for(int i=0;i<3;i++)
  {
    for (int j = 0;j<3;j++)
    {
      gsl_matrix_set(A,i,j,a_data[k]);
      gsl_matrix_set(A_copy,i,j,a_data[k]);
      k++;
    }
  }
  gsl_linalg_LU_decomp (A, p, &s); //This function mutates A to an LU form
  gsl_permutation_free (p);
  /*
Since the LU decompsition function mutates A such that the upper triangle including the diagonal is U while the lower triangle excluding the
diagonal is L. The diagonal of L has 1.0 and is not stored.
Using this fact we have seperated the L and U matrices from A
  */

  for(int i=0;i<3;i++)//This Section L and U from A
  {
    for (int j = 0;j<3;j++)
    {
     if(i>j)
     gsl_matrix_set(L,i,j,gsl_matrix_get(A,i,j));
     else if (i==j)
     {
      gsl_matrix_set(U,i,j,gsl_matrix_get(A,i,j));
      gsl_matrix_set(L,i,j,1.0);
     }
     else
      gsl_matrix_set(U,i,j,gsl_matrix_get(A,i,j));
    }
  }

  printf("Modified A Matrix due to LU computation : \n");
  show(A,3);

  printf("The L Matrix\n");
  show(L,3);

  printf("The U Matrix\n");
  show(U,3);
//Prod Matrix stores the product and verifies that the Matrix is same.
  Prod = mat_mul(L,U,3);
  printf("Product of L and U\n");
  show(Prod,3);

  printf("Original\n");
  show(A_copy,3);

  /*To check explicity we use the function we use the GSL matrix equality checker to verify our claim*/

  if( gsl_matrix_equal(A_copy,Prod) == 1)
    printf("The Matrices are indeed equal, verified by gsl_matrix_equal()\n");
  else
    printf("The Matrices are not equal, verified by gsl_matrix_equal()\n");

  return 0;
}
