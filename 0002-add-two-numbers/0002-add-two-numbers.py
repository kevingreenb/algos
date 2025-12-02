# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            carry = s // 10
            s = s % 10
            ans.next = ListNode(s)
            ans = ans.next
        
        while l1:
            s = l1.val + carry
            l1 = l1.next
            carry = s // 10
            s = s % 10
            ans.next = ListNode(s)
            ans = ans.next              
            
        while l2:
            s = l2.val + carry
            l2 = l2.next
            carry = s // 10
            s = s % 10
            ans.next = ListNode(s)
            ans = ans.next  

        if carry:
            ans.next = ListNode(carry)

        return dummy.next

        