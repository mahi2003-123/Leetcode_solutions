class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for char in nums:
            freq[char]=freq.get(char,0)+1
        m= max(freq,key=freq.get)
        return m
        