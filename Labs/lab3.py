import random
import math

# computes x^y mod N
def modexp(x,y,N):
    if y == 0: 
        return 1
    z = modexp(x,math.floor(y/2),N)
    if y%2 == 0:
        return (z**2) % N
    else:
        return x * (z**2 % N)

# determines if a number is prime by testing to see if it is coprime with other numbers    
def primality2(N,k):
    arr = []
    prime  = True
    count = 0 # counts the number of times it believes the number is prime when its not (# of values that aren't coprime with N)
    # generate random numbers for the comparison
    for i in range(k):
        arr.append(random.randint(1,N-1))       
    for a in arr:
        # if the number is not coprime with another number, it is certainly not prime
        if modexp(a,N-1,N) != 1:
            count+=1
            prime = False
    print("Coprime with",count,"numbers." )
    # (1-(count/k)) because we're counting the number of times
    print("Probability prime:",(1-(count/k)))
    return prime
    
if __name__ == "__main__":
    #arr = [12,23,14,73,31,19,22]
    # Carmichael numbers are not prime, but coprime with a lot of numbers
    arr = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    for a in arr:
        if primality2(a,1000) == False :
            print(a,"is not prime.\n")
        else:
            print(a,"is prime.\n")
