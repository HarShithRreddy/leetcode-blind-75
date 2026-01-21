"""
Problem: 33. Search in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search

Approach:
- Perform a modified binary search on the rotated array
- At each step, determine which half of the array is sorted
- If the target lies within the sorted half, discard the other half
- Otherwise, search the unsorted half
- Repeat until the target is found or the search space is exhausted

Time Complexity: O(log n)
Space Complexity: O(1)

Note:
At every iteration, at least one half of the array is guaranteed to be sorted.
The algorithm exploits this property to maintain logarithmic time complexity.
"""

class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while(start <= end):
            middle = (start + end) // 2

            if(nums[middle] == target):
                return middle
            if(nums[start] <= nums[middle]):
                if(nums[start] <= target < nums[middle]):
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if(nums[middle] < target <= nums[end]):
                    start = middle + 1
                else:
                    end = middle - 1

        return -1

            