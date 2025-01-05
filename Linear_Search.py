def Linear_search(arr,x):
    for i in range(len(arr)):
        if arr[x]==x:
            return i
    return -1


n=int(input("Enter the size of array:"))
arr=[]
for i in range(0,n):
    ele=int(input("Enter the element"))
    arr.append(ele)

x=int(input("Enter the element to be searched:"))
result=Linear_search(arr,x)
if result!=-1:
    print("Element found at index ",i)
else:
    print("Element not found")
