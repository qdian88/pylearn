n=int(input())
love=input().split()
love=[int(i) for i in love]
result=[0,]
for i in range(1,len(love)):
    a=0
    for j in love[:i]:
        if j<love[i]:
            a+=1
    result.append(a)
[print(i,end=" ") for i in result]