"""
Problem: 49. Group Anagrams
Difficulty: Medium
Category: Arrays / Hashing

Approach:
- Iterate through each string in the input list
- For each string, compute an anagram pattern by sorting its characters
- Use the sorted string as a key in a dictionary
- Append the original string to the list corresponding to that key
- Return all grouped anagram lists from the dictionary

Time Complexity: O(n * k log k)
- n = number of strings
- k = maximum length of a string (sorting each string)

Space Complexity: O(n * k)
- Used for storing grouped strings in a hash map

Note:
The order of groups and the order of strings within each group does not matter.
"""
class Solution:
    def groupAnagrams(self,strs):
        strngs={}
        for i in strs:
            key = "".join(sorted(i))
            if key not in strngs:
                strngs[key] = []

            strngs[key].append(i)
        output=[]
        for i in strngs:
            output.append(strngs[i])
        return(output)

