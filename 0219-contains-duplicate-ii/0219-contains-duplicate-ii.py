class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        sceen ={}
        for i in range(len(nums)):
            if nums[i] in sceen:
                if abs(i-sceen[nums[i]])<=k:
                    return True
        
            sceen[nums[i]]=i
        return False
        