class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in t:
                t = t.replace(ch,"",1)
            else: 
                return False
        return True