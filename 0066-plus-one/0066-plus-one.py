class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = deque()
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            current = 0
            if i == len(digits) - 1:
                current = (digits[i] + 1) % 10
                carry = (digits[i] + 1) // 10
            else:
                current = (digits[i] + carry) % 10
                carry = (digits[i] + carry) // 10
            q.appendleft(current)
        if carry:
            q.appendleft(1)
        return list(q)