class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        window = 0
        ans = float('inf')

        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                ans = min(ans, right - left + 1)
                window -= nums[left]
                left += 1

        if ans == float('inf'):
            return 0

        return ans