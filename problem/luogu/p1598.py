n_l=[0 for i in range(26)]
for i in range(4):
    s=input()
    for j in s:
        l=ord(j)-ord("A")
        if l>=0 and l<=25:
            n_l[l]+=1
pr=[]
s=""
for i in range(25):
    s+=chr(ord("A")+i)+" "
s+="Z"
pr.append(s)
for i in range(max(n_l)):
    s=""
    for j in range(25):
        if n_l[j]>i:
            s+="* "
        else:
            s+="  "
    if n_l[25]>i:
        s+="*"
    else:
        s+=" "
    pr.append(s)
[print(i) for i in pr[::-1]]