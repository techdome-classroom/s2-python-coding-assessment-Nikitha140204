class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to match the opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of opening brackets
        stack = []

        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # Check if the stack is empty (all brackets matched)
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))      # Output: False
