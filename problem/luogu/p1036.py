def C1(L,k):
    if k==1:
        return([[i] for i in L])
    elif k==len(L):
        return([L])
    else:
        return(C1(L[:-1],k)+[i+[L[-1]] for i in C1(L[:-1],k-1)])

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


s=input().split() #输入总元素个数n及要选取的元素个数k
n=int(s[0])
k=int(s[1])
s=input().split() #输入n个整数，用空格分开
L=[int(i) for i in s]
A=C1(L,k)
N=0
for i in A:
    sum=0
    for j in i:
        sum+=j
    if isPrime(sum):
        N+=1
print(N)