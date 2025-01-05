def isPalindrome(x):
    if x < 0:
        return False
    # negative numbers cannot be a palindrome
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = (reversed_num * 10) + digit
        x = x // 10
    return original == reversed_num

num = int(input())

if isPalindrome(num):
    print(str(num) + " is a palindrome")
else:
    print(str(num) + " is not a palindrome")