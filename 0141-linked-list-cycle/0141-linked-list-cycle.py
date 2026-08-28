# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        sceen=set()
        current = head
        while current:
            if current in sceen:
                return True
            sceen.add(current)
            current=current.next
        return False

        
        