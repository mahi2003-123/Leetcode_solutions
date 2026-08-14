class Solution(object):
    def maxProfit(self, prices):
        slow=0
        a=0

        for fast in range(1,len(prices)):
            if prices[fast]<prices[slow]:
                slow=fast
            else:
                deal=prices[fast]-prices[slow]
                a=max(a,deal)
        return a
               
        



        