import numpy as np
import timeit as ti
import ubelt as ub

# Runtime: O(n^3)
def matrix_mult(A,B,n):
    # initialize the n x n matrix C
    C = []
    for i in range(n):
        C.append(np.zeros(n))
    
    # for every row in A
    for i in range(n): 
        # for every column in B
        for j in range(n):
            for k in range(n):
                # sum up the products for each row/col multiplication
                C[i][j] += A[i][k] * B[k][j]
    return np.matrix(C)

# Strassen's algorithm
def matrix_mult2(X,Y,n):
    if n == 1:
        return X*Y
    else:
        Z = []
        A = X[0:(n//2),0:(n//2)]
        B = X[0:(n//2),(n//2):n]
        C = X[(n//2):n,0:(n//2)]
        D = X[(n//2):n,(n//2):n]
        E = Y[0:(n//2),0:(n//2)]
        F = Y[0:(n//2), (n//2):n]
        G = Y[(n//2):n, 0:(n//2)]
        H = Y[(n//2):n, (n//2):n]
        
        P1 = matrix_mult2(A,(F - H),n/2)
        P2 = matrix_mult2((A + B), H,n/2)
        P3 = matrix_mult2((C+D),E,n/2)
        P4 = matrix_mult2(D,(G - E),n/2)
        P5 = matrix_mult2((A+D),(E+H),n/2)
        P6 = matrix_mult2((B-D),(G+H),n/2)
        P7 = matrix_mult2((A-C),(E+F),n/2)
        
        Z11 = P5 + P4 - P2 + P6
        Z12 = P1 + P2
        Z21 = P3 + P4
        Z22 = P1 + P5 - P3 - P7
        Zup = np.hstack((Z11,Z12))
        Zlow = np.hstack((Z21,Z22))
        Z = np.vstack((Zup,Zlow))
        return Z
    
if __name__ == "__main__":
    n = int(input("Enter a value for n: "))
    # n is the user input, the other numbers are test cases
    # n is assumed to be a power of 2
    m = [n,16, 32, 64, 128, 256, 512, 1024]
    times1 = []
    times2 = []
    # create 2 n x n matices with values of 0 or 1
    A = np.random.rand(m[0], m[0])
    B = np.random.rand(m[0], m[0])
    # print the resulting matrix from the multiplication
    #print(matrix_mult(A,B,m[0]))
    #print(matrix_mult2(A,B,m[0]))
    for num in m:
        A = np.random.rand(num, num)
        B = np.random.rand(num, num)
        for t in ub.Timerit(3,label = "time1"):
            with t:
                matrix_mult(A,B,num)

        for t in ub.Timerit(3,label = "time2:"):
            with t:
                matrix_mult2(A,B,num)