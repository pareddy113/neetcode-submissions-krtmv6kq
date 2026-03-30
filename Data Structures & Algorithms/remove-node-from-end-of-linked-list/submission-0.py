# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        start = head
        while start:
            size = size + 1
            start = start.next
        nodeIndex = size - n
        print(nodeIndex)
        count = 0
        prev = ListNode(0)
        new = prev.next = curr = head
        while curr:
            if(count == nodeIndex):
                # [0, 5], count=0
                temp = curr.next # none
                prev.next = temp # []
                break
            else:
                prev = prev.next
                curr = curr.next
                count = count + 1
        if(nodeIndex == 0):
            return prev.next
        else:
            return head


        