# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(list_node):
            cur, prev = list_node, None
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        first, second = head, reverse(slow.next)
        slow.next = None

        while first and second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
        
        return head
        