class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        d = {}
        ptr = head
        while ptr:
            d[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr:
            if ptr.next:
                d[ptr].next = d[ptr.next]
            if ptr.random:
                d[ptr].random = d[ptr.random]
            ptr = ptr.next
        
        return d[head]