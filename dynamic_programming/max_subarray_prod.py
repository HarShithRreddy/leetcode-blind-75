class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            temp_max = max(x, x * max_prod, x * min_prod)
            temp_min = min(x, x * max_prod, x * min_prod)

            max_prod = temp_max
            min_prod = temp_min

            result = max(result, max_prod)

        return result