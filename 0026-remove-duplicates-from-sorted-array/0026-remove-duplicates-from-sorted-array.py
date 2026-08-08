class Solution(object):
    def removeDuplicates(self, nums):
         slow = 0
         fast = 1
         for fast in range(len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
                
         return slow + 1



        