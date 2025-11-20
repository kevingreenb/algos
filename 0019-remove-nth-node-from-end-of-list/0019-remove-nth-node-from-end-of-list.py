# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        current, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            current = current.next
            fast = fast.next

        current.next = current.next.next
        return dummy.next
        
        