"""
Problem: 242. Valid Anagram
Difficulty: Easy
Category: Arrays / Hashing

Approach:
- First check if both strings contain the same set of characters
- Use two dictionaries to count the frequency of each character in both strings
- Compare the frequency of every character
- If all frequencies match, the strings are anagrams

Time Complexity: O(n)
Space Complexity: O(n)

Note:
This problem can be optimized using a single dictionary or sorting,
but the current approach prioritizes clarity and correctness.
"""

class Solution:
    def isAnagram(self,s,t):
        content={}
        content2={}
        if(set(s)!=set(t)):
            return False
        for i in s:
            content[i]=0
        for i in t:
            content2[i]=0
        for i in s:
            content[i]+=1
        for i in t:
            content2[i]+=1
        for i in s:
            if(content[i]!=content2[i]):
                return False
        return True
