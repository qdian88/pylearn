k=int(input())
for i in range(10000,30001):
    a=i//100
    b=i//10-i//10000*1000
    c=i%1000
    n=0
    if a%k==0 and b%k==0 and c%k==0:
        print(i)
        n+=1
if n==0:
    print('No')