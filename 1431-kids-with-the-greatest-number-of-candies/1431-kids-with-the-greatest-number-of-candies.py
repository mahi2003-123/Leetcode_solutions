class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        large = 0
        arr = []
        large=max(candies)
        
        
        for i in candies:
            if i+extraCandies>=large:
                arr.append(True)
            else:
                arr.append(False)
        return arr


        