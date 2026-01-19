"""
Problem: 20. Valid Parentheses
Difficulty: Easy
Category: Stack

Approach:
- Use a stack to track opening brackets
- Push opening brackets onto the stack
- On encountering a closing bracket:
  - Check if the stack is empty (invalid case)
  - Pop the top element and verify it matches the closing bracket
- After processing all characters, the stack must be empty for the string to be valid

Time Complexity: O(n)
Space Complexity: O(n)

Note:
Early exit is used when an invalid closing bracket is encountered.
"""

class Solution:
    def isValid(self, s):
        opening="({["
        closing=")}]"
        stack=[]
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if(stack==[]):
                    return False
                p=stack.pop()
                if(p=='(' and i!=')'):
                    return False
                if(p=='{' and i!='}'):
                    return False
                if(p=='[' and i!=']'):
                    return False
        if(stack!=[]):
            return False
        return True