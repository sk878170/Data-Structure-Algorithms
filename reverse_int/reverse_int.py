# Given an integer, you need to reverse it without using string.

def reverse(n):
    if n == 0:
        return 0
    else:
        rev=0
        while n>0:
            rev = rev*10 + n%10 
            n = n//10 
    return rev
        

# rev = 0 * 10 + 123 % 10 = 3 -> n = 123//10 -> 12
# rev = 3*10 + 12 % 10 = 30+2 = 32  -> n =12//10 = 1
# rev = 32*10 + 1//10 = 320+1 = 321 -> n = 1//10 = 0
# n =0, while loop terminates

n= 123
res=reverse(n) 
print(res) 

# Time complxity : O (d), where d is number of digits
# Time complexity (in terms of n) : O(log10(n))
# Space complexity : O(1) as we are not using any extra space.