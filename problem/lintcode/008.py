'''
A="abcdefgh"
for i in range(3):
    temp=A[-1]
    A=temp+A[0:len(A)-1]
print(A)
'''
def AA(str):
    for i in range(3):
        temp=str[-1]
        str=temp+str[0:len(str)-1]
    print(str)
    return(str)
A="abcdefgh"
A=AA(A)
print(A)
