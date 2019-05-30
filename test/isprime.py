def isPrime(_n):
    Primes=[2,3,5,7,11,13,17,19,23,29,31,37]
    if _n<2:
        return(False)
    elif _n in Primes:
        return(True)
    sq=int(_n**(1/2))
    if sq>37:
        for i in range(39,sq+2,2):
            if isPrime(i):
                Primes.append(i)
    isprime=True
    for i in Primes:
        if i*i>_n:
            break
        elif _n%i==0:
            isprime=False
            break
    return(isprime)
N=0
for i in range(1000,20000):
    if isPrime(i):
        print(i,end="  ")
        N+=1
print(N)