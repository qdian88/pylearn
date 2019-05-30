s=input().split()
l=int(s[0])
n=int(s[1])
tree=[]
for i in range(l+1):
    tree+=[1]
for i in range(n):
    s=input().split()
    for j in range(int(s[0]),int(s[1])+1):
        tree[j]=0
sum=0
for i in tree:
    sum+=i
print(sum)