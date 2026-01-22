"""
Problem: 53. Maximum Subarray
Difficulty: Medium
Category: Dynamic Programming (Kadane’s Algorithm)

Approach:
- Maintain a running sum of the current subarray
- At each step, decide whether to extend the current subarray
  or start a new one from the current element
- Track the maximum sum encountered so far

Key Insight:
If the current subarray sum becomes worse than starting fresh,
discard it and restart from the current element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums):
        currentSum=-10000
        maxSum=-10000
        for i in nums:
            currentSum=max(currentSum+i,i)
            maxSum=max(maxSum,currentSum)
        return maxSum