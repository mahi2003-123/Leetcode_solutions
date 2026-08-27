class Solution(object):
    def maxProfit(self, prices):
        a=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                a+=prices[i]-prices[i-1]
        return a
                
        