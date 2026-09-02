class Solution(object):
    def jump(self, nums):
        farmost=0
        j=0
        current=0
        for i in range(len(nums)-1):
            farmost=max(farmost,i+nums[i])

            if i==current:
                j+=1
                current=farmost
        return j
        