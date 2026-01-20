"""
Problem: 704. Binary Search
Difficulty: Easy
Category: Binary Search

Approach:
- Use two pointers (left and right) to define the current search space
- Repeatedly calculate the middle index
- If the middle element matches the target, return its index
- If the target is smaller, search the left half
- If the target is larger, search the right half
- If the search space becomes invalid, return -1

Time Complexity: O(log n)
Space Complexity: O(1)

Note:
The loop condition must be `left <= right` to ensure the last element
in the search space is checked.
"""

class Solution:
    def search(self,List, target):
        start=0
        end=len(List)-1
        while(start<=end):
            middle= int((start+end)/2)
            if(List[middle]==target):
                return middle
            elif(List[middle]<target):
                start=middle+1
            else:
                end=middle-1
        return -1
