def qsort(M):
    if len(M) <= 1:
        return(M)
    a = M[0]
    less = []
    high = []
    for i in M[1:]:
        if i < a:
            less.append(i)
        else:
            high.append(i)
    return(qsort(less)+[a]+qsort(high))


s = input().split()
s = [int(i) for i in s]
s = qsort(s)
print(s)
