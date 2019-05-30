A=[2,3,1,9,12,65,47,46,86,53,57,86,12,35,79,98,73,59]
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
A=qsort(A)
print(A)