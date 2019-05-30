#输入两个整数m,n，输出第m个质数到第n个质数中的所有质数
s=input().split()
m=int(s[0])
n=int(s[1])
p=[2,3]
i=5
t=2
while t<=n:
        j=0
        s=i**(1/2)
        isp=True
        while p[j]<=s:
                if i%p[j]==0:
                        isp=False
                j+=1
        if isp==True:
                p.append(i)
                t+=1
        i+=2
for _ in range(m-1,n):
        if (_-m+2)%20==0:
                print(p[_],end="\n")
        elif _==n-1:
                print(p[_],end="")
        else:
                print(p[_],end=" ")
