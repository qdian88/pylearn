s=input().split()
a=int(s[0])
b=int(s[1])
Ps=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,51]
for i in range(3,b+1,2):
    isprime=True
    sq=int(i**(1/2))
    for j in Ps:
        if j*j>i:
            break
        elif i%j==0:
            isprime=False
            break
    if isprime and i>Ps[-1]:
        Ps.append(i)
for i in range(a,b+1):
    if i in Ps:
        index=Ps.index(i)
        break
for i in Ps[index:]:
    if str(i)==str(i)[::-1]:
        print(i)