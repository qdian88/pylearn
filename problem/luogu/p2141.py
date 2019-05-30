n = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]


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


numbers = qsort(numbers)
times = 0
for i in numbers[2:]:
    for j in numbers:
        founded=False
        if j >i//2:
            break
        else:
            for k in numbers[numbers.index(j)+1:]:
                if j+k == i:
                    times += 1
                    founded=True
                elif j+k > i:
                    break
        if founded==True:
            break
print(times)
