#Given an array of integers nums and an integer target, return indices of two numbers such that they add up to a target.
# Assume that each input would have exactly one solution and you cannot use same element twice.

def twoSum(nums, target):
    arr={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in arr:
            return [arr[complement],i]
        arr[num]=i

# Take input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("Input array:", nums)

target= int(input("Enter the target: "))

sum=twoSum(nums, target)
print(sum)
