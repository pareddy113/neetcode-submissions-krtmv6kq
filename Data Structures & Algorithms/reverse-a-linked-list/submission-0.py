# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# None -> 1 -> 2 -> 3

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevN, nextN = None, head
        while nextN is not None:
            temp = nextN.next
            nextN.next = prevN
            prevN = nextN
            nextN = temp
        return prevN
        

        