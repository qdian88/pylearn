nums=[2,7,11,15]
target = 9
L=len(nums)
sums=[]
finded=0
for i in range(L):
    for j in range(L):
        if nums[i]+nums[j]==target:
            finded=1
            print(i,j)
            break
    if finded==1:
        break