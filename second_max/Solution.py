# Given an array find the second largest number in it
def second_Max(arr):
    max =0
    max2 = 0
    # max will store the largest number found, while max2 stores second largest 
    for i in arr:
        if i > max: # iterate and compare each element in array, if current element is greater than max, then max is declared new largest no
            max=i
        elif i > max2 and max !=max2: # Now max is largest element. but if current element is greater than max2 and max2 , max are diff
            max2=i # declare max2 largest
    return max2

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
res=second_Max(arr)
print(res)