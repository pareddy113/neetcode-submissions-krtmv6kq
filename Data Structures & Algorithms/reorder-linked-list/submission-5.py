# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        
        curr = first.next
        prev = first.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        # prev - last index
        # head - first index
        left, right = head, prev
    
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2


