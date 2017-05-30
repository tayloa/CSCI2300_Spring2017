import random
import math
import timeit

def method1(x,y):
    answer = 0
    ## for each bit in y (reversed)
    ## check if the y bit is on (1), if so add x to the final result
    while (y != 0):
        if y & 1:
            answer += x
        ##left shift (multiple x * 2^1)
        x<<=1
        ##left shift
        y>>=1
    return answer

def method2(x,y):
	if y == 0: 
		return 0 
	z = method2(x, math.floor(y/2)) 
	if (y%2) == 0:
		return 2*z
	else:
		return x + 2*z
	    
def method3(x,y):
    ## n is the max number of bits in the number
    n = max(x.bit_length(),y.bit_length())
    if (n == 1): 
	    return x*y
    if x ==0 or y == 0:
	    return 0 
    ## number of bits you're shifting left by
    nR = math.floor(n/2)    
    ## split each number into left and right bits 
    ## leftmost (ceiling of n/2) and righmost (floor of n/2)   
    ## shift right by the floor to get the right half
    ## create a mask by shifting left on 1 by floor(n/2), then subtract 1
    ## & the original number and the mask to get the left side
    
    xL = x >> nR
    m = xL << nR
    xR = x - m
    
    yL = y >> nR
    m = yL << nR
    yR = y - m    
    
    
    P1 = method3(xL, yL)
    P2 = method3(xR, yR)
    P3 = method3(xL + xR, yL + yR)
    return P1 * (2**(2*nR)) + (P3 - P1 - P2) * 2**(nR) + P2

if __name__ == "__main__":
    d = int(input('Number of digits: '))
    m1_times = []
    m2_times = [] 
    m3_times = []
    print(method1(10,8))
    print(method2(10,8))
    print(method3(10,8))
    for i in range(10):
	    a = b = ''
	    for j in range(d):
		    a += str(random.randint(1,9))
		    b += str(random.randint(1,9))
	    print("Trial",i+1,":","a =",a,"b =",b)
	    m1_times.append(timeit.timeit('method1(' + a +',' + b + ')', 'from __main__ import method1', number=1))
	    m2_times.append(timeit.timeit('method2(' + a +',' + b + ')', 'from __main__ import method2', number=1))
	    m3_times.append(timeit.timeit('method3(' + a +',' + b + ')', 'from __main__ import method3', number=1))
    average_m1 = float(sum(m1_times))/10
    average_m2 = float(sum(m2_times))/10
    average_m3 = float(sum(m3_times))/10
    print("Average Times:","\n\tMethod 1:",average_m1,"\n\tMethod 2:",average_m2,"\n\tMethod 3:",average_m3)
    
    # starts failing at 200 digits
 
 