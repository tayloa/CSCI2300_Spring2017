import timeit as ti
import matplotlib.pyplot as plt

def fib1(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib1(n-1)+fib1(n-2)

def fib2(n):
	f = [0,1]
	for i in range(2,n+1):
		f.append(f[i-1] + f[i-2])
	return f[n]

if __name__ == "__main__":
	temp1 = [1,5,10,15,20,25,30,35,40,41,43]	
	temp2 = [2**10,2**12,2**14,2**16,2**18][0:5]#,2**19]
	
	fib1_time = []
	fib2_time = []
	for n in temp1:
	    time1 = (ti.timeit('fib1(' + str(n) + ')','from __main__ import fib1',number=1))
	    fib1_time.append(time1)
	for n in temp2:
	    time2 = (ti.timeit('fib2(' + str(n) + ')','from __main__ import fib2',number=3))
	    fib2_time.append(time2)
    
	#plt.plot(temp1, fib1_time,'r')
	plt.plot(temp2, fib2_time,'b')
	plt.show()	