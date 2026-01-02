# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0 
        current = head
        while current and count < k:
            count += 1
            current = current.next
        if count < k:
            return head
        current, previous = head, None
        for _ in range(k):
            next = current.next
            current.next = previous 
            previous = current
            current = next
        head.next = self.reverseKGroup(current, k)
        return previous
        