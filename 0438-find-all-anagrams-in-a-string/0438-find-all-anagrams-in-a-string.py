class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        k = len(p)

        if len(s) < k:
            return res

        count_p = [0] * 26
        count_win = [0] * 26

        for char in p:
            count_p[ord(char) - ord('a')] += 1

        for right in range(len(s)):
            count_win[ord(s[right]) - ord('a')] += 1

            if right >= k:
                count_win[ord(s[right-k]) - ord('a')] -= 1

            if count_win == count_p:
                res.append(right-k+1)

        return res