length=int(input())
lst=[]
for i in range(length):
    lst.append(int(input()))

maxi=0
for i in lst:
    if i>maxi:
        maxi=i

print("The largest element is",maxi)
