#p1055  测试10组数据，有4组通不过，原因还未找到
s=input().split("-")
L=s[0]+s[1]+s[2]
if s[3]=="X":
    a=10
else:
    a=int(s[3])
Sum=0
for i in range(len(L)):
    Sum+=int(L[i])*(i+1)
if Sum%11==a:
    print("Right")
elif Sum%11==10:
    b="X"
    print(s[0]+"-"+s[1]+"-"+s[2]+"-"+b)
else:
    b=str(Sum%11)
    print(s[0]+"-"+s[1]+"-"+s[2]+"-"+b)