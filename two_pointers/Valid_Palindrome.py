"""
Problem: 125. Valid Palindrome
Difficulty: Easy
Category: Two Pointers

Approach:
- Convert the string to lowercase to make the check case-insensitive
- Build a new string containing only alphanumeric characters
- Use two pointers to compare characters from the beginning and end
- If any mismatch is found, return False
- If all characters match, return True

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def isPalindrome(self,strng):
        strng=strng.lower()
        new_str=""
        alpha="abcdefghijklmnopqrstuvwxyz0123456789"
        for i in strng:
            if(i in alpha):
                new_str+=i
        for i in range(0,int(len(new_str)/2)):
            if(new_str[i]!=new_str[len(new_str)-i-1]):
                return False
        return True
