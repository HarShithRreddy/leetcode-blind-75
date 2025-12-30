"""
Problem: 217. Contains Duplicate
Difficulty: Easy
Category: Arrays / Hashing

Approach:
- Use a dictionary to count occurrences of each element
- If any element appears more than once, return True
- Otherwise, return False

Time Complexity: O(n)
Space Complexity: O(n)

Note:
This solution can be optimized using a set with early exit,
but the current approach prioritizes clarity and correctness.
"""
class Solution:
    def duplicate(self,nums):
        count_dict={}
        for i in range(0,len(nums)):
            count_dict.setdefault(nums[i],0)
            count_dict[nums[i]]+=1
        print(count_dict)
        for i in count_dict:
            if(count_dict[i]==1):
                continue
            else:
                return True
        return False