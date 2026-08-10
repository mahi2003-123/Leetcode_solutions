class Solution(object):
    def numRescueBoats(self, people, limit):
        left=0
        right=len(people)-1
        c=0
        people.sort()
        while left<=right:
            if people[left]+people[right]>limit:
                right-=1
                c+=1
            else:
                right-=1
                left+=1
                c+=1
        return c
        

        
        