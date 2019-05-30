star=input()
team=input()
s=1
t=1
for i in star:
    s*=ord(i)-ord("A")+1
for j in team:
    t*=ord(j)-ord("A")+1
if (s-t)%47==0:
    print("GO")
else:
    print("STAY")