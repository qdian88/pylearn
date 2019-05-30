s=input().split()
s=[int(i) for i in s]
h=int(input())
def qsort(M):
    if len(M)<=1:
        return M
    else:
        less=[]
        great=[]
        for i in range(1,len(M)):
            if M[i]<=M[0]:
                less+=[M[i]]
            else:
                great+=[M[i]]
        return qsort(less)+[M[0]]+qsort(great)
s=qsort(s)
n=0
for j in s:
    if j<=h+30:
        n+=1
    else:
        break
print(n)