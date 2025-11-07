def binarySearch(arr, k,l,h):
    if l > h:
        return -1
    else:
        mid=l+(h-l)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return binarySearch(arr, k, mid + 1, h)
        else:
            return binarySearch(arr, k, l, mid - 1)

lst=[]
n=int(input("Enter the size of the list \n"))
for i in range(n):
    x=int(input("Enter the element : "))
    lst.append(x)
key=int(input("Enter the element to be searched: "))
l=0
h=len(lst)-1
result=binarySearch(lst,key,l,h)
print(result)


