# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            current.next = ListNode(val)
            current = current.next
            l1, l2 = l1.next, l2.next
        while l1:
            val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10  
            current.next = ListNode(val)
            current = current.next
            l1 = l1.next          
        while l2:
            val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            current.next = ListNode(val)
            current = current.next
            l2 = l2.next
        if carry:
            current.next = ListNode(carry)
        return dummy.next                       