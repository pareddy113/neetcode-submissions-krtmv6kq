# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeLists(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        head = sortedList = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
            sortedList = sortedList.next            
    
        if list1:
            sortedList.next = list1
        if list2:
            sortedList.next = list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # mergedList = merge(l1, l2)
        # merge(mergedList, l3)..
        if not len(lists):
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])
        return lists[len(lists)-1]
        