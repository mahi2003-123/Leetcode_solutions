class Solution(object):
    def containsDuplicate(self, nums):
        newset = set()

        for n in nums:
            if n in newset:
                return True
            newset.add(n)
        
        return False
        