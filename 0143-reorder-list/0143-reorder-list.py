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
        def reverse(node):
            current, previous = node, None
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            return previous
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        first = head
        second = reverse(second)
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second  = first_next, second_next