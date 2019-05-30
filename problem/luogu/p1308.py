#此方法效率太低，试一试
word=input().lower()
paper=input().lower()
d=len(word)
l=len(paper)
first=-1
n=0
for i in range(l-d):
    w=paper[i:i+d]
    if w==word:
        if i!=0 and i!=l-d:
            if paper[i-1]==" " and paper[i+d]==" " and first==-1:
                n+=1
                first=i
            elif paper[i-1]==" " and paper[i+d]==" ":
                n+=1
        elif i==0 and i!=l-d:
            if paper[i+d]==" " and first==-1:
                n+=1
                first=i
            elif paper[i+d]==" ":
                n+=1
        elif i!=0 and i==l-d:
            if paper[i-1]==" " and first==-1:
                n+=1
                first=i
            elif paper[i-1]==" ":
                n+=1
if first!=-1:
    print(n,first)
else:
    print(first)