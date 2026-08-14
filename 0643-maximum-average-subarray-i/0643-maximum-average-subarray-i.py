class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        window=0
        a=float('-inf')
        avg=0
        for right in range(len(nums)):
            window+=nums[right]
            if right-left+1==k:
                avg = float(window)/k
                a=max(a,avg)
                window-=nums[left]
                left+=1
        return a
        