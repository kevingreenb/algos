# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # push (value, index, node) so ties on value are resolved by index
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        ptr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            ptr.next = node
            ptr = ptr.next
            if node.next:
                # use the same index or a new unique counter; using i is fine here
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
              