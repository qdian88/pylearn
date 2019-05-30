n=int(input())
s=input()
letter="abcdefghijklmnopqrstuvwxyz"
password=""
for i in s:
    index=(ord(i)-ord("a")+n)%26
    password+=letter[index]
print(password)
