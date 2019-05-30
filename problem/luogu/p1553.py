s=input()
T=0 #记录类型，0--整数，1--小数，2--分数，3--百分数
for i in s:
    if i==".":
        T=1
        break
    elif i=="/":
        T=2
        break
    elif i=="%":
        T=3
        break
def change(s,T=0):
    if T==1:
        s=str(int(s))
    l=len(s)
    n=int(s)
    result=0
    for i in range(l):
        result+=(n%10)*(10**(l-i-1))
        n=n//10
    return(str(result))
if T==0:
    print(change(s))
elif T==1:
    s=s.split(".")
    print(change(s[0])+"."+change(s[1],T))
elif T==2:
    s=s.split("/")
    print(change(s[0])+"/"+change(s[1]))
elif T==3:
    s=s[:len(s)-1]
    print(change(s)+"%")
