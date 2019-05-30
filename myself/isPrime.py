def isPrime(_n):
    Ps=[2,3,5,7,11,13,17,19,23,29]
    if _n<2:
        return(False)
    elif _n in Ps:
        return(True)
    isprime=True
    sq=int(_n**(1/2))
    if sq>29:
        for i in range(31,sq+2,2):
            if isPrime(i):
                Ps.append(i)
    for i in Ps:
        if i*i>_n:
            break
        elif _n%i==0:
            isprime=False
            break
    return(isprime)