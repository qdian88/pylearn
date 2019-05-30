s = input().split("-")
L = s[0] + s[1] + s[2]
print(L)
if s[3] == "X":
    a = 10
else:
    a = int(s[3])
print(a)
Sum = 0
for i in range(len(L)):
    Sum += int(L[i]) * (i + 1)
print(Sum)
if Sum % 11 == a:
    print("Right")
elif Sum % 11 == 10:
    b = "X"
print(s[0] + "-" + s[1] + "-" + s[2] + "-" + b)
else:
    b = str(Sum % 11)
print(s[0] + "-" + s[1] + "-" + s[2] + "-" + b)
