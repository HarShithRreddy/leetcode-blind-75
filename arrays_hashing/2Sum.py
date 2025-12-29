"""
Problem: Two Sum
Pattern: Hash Map (One-pass)

Approach:
- Traverse the list once
- For each element, compute the value needed to reach the target
- Check if this value has already been seen
- Store previously seen values with their indices

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def two_sum(self,nums,target):
        solution=[]
        sol_dict={}
        value=0
        for i in range(0,len(nums)):
            value=target-nums[i]
            if value in sol_dict:
                solution.append(nums.index(value))
                solution.append(i)
            else:
                sol_dict[nums[i]]=value
        return solution
