class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sceen=set()
        slow=0
        maxi=0
        for fast in range(len(s)):
            while s[fast] in sceen:
                
                sceen.remove(s[slow])
                slow+=1
            sceen.add(s[fast])
            if maxi<len(sceen):
                    maxi=len(sceen)
        return maxi


        