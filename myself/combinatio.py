def C1(L,k):
    #从列表L中选出k个元素，返回所有可能组成的列表
    #递归实现
    if k==1:
        return([[i] for i in L])
    elif k==len(L):
        return([L])
    else:
        return(C1(L[:-1],k)+[i+[L[-1]] for i in C1(L[:-1],k-1)])
