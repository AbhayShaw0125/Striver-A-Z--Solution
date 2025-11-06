def binarySearch(arr, x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low +(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    else:
        return -1

lst=[]
n=int(input("Enter the size of the list \n"))
for i in range(n):
    x=int(input("Enter the element : "))
    lst.append(x)
key=int(input("Enter the element to be searched: "))
result=binarySearch(lst,key)
print(result)


