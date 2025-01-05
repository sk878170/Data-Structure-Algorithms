class Solution:
    def romantoInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        for char in reversed(s):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        return total

    def inttoRoman(self, s: int) -> str:
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ''
        for value in roman.keys():
            while s >= value:
                result += roman[value]
                s -= value
        return result

# Initialize ans variable
ans = 'y'

while ans == 'y':
    print("Menu\n1. Roman to Integer\n2. Integer to Roman")
    choice = int(input("Enter your choice: "))

    # Create instance of Solution class
    sol = Solution()

    if choice == 1:
        roman_number = input("Enter the Roman number: ")
        result = sol.romantoInt(roman_number)
        print(f"The integer value of {roman_number} is: {result}")
    elif choice == 2:
        integer_number = int(input("Enter the integer: "))
        result = sol.inttoRoman(integer_number)
        print(f"The Roman numeral for {integer_number} is: {result}")
    else:
        print("Invalid choice!")

    ans = input("Quit[y/n]: ")
