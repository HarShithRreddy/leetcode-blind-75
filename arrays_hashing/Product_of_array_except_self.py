"""
Problem: 238. Product of Array Except Self
Difficulty: Medium
Category: Arrays / Prefix-Suffix

Approach:
- Build a prefix product array where each index stores the product of elements to the left
- Build a suffix product array where each index stores the product of elements to the right
- For each index, multiply its prefix and suffix values to get the result
- This avoids using division and runs in linear time

Time Complexity: O(n)
Space Complexity: O(n)

Note:
This solution uses additional prefix and suffix arrays for clarity.
It can be optimized to O(1) extra space by reusing the output array.
"""

class Solution:
    def productExceptSelf(self,nums):
        left=[]
        left.append(1)
        left.append(nums[0])
        right=[]
        for i in range(0,len(nums)):
            right.append(0)
        right[-1]=1
        right[-2]=nums[-1]
        for i in range(2,len(nums)):
            left.append(left[i-1] * nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        sol=[]
        for i in range(0,len(nums)):
            sol.append(left[i]*right[i])
        return(sol)
s=Solution()
print(s.productExceptSelf([1,2,3,4]))
