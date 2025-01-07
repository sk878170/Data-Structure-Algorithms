class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # Map closing brackets to their corresponding opening brackets

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Get the top element or a placeholder
                if mapping[char] != top_element:  # Check if it matches the expected opening bracket
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        return not stack  # Stack should be empty for the string to be valid


# Test the Solution
if __name__ == "__main__":
    solution = Solution()
    test = "()[]{}"
    if solution.isValid(test):
        print("Valid")
    else:
        print("Invalid")
