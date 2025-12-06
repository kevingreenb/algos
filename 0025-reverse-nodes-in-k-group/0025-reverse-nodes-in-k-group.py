# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First, check if we have k nodes to reverse
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        # If we don't have k nodes, return head as-is
        if count < k:
            return head
        
        # Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # head is now the tail of the reversed section
        # Connect it to the result of reversing the rest
        head.next = self.reverseKGroup(curr, k)
        
        # prev is the new head of this reversed section
        return prev
        