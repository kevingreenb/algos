class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        left = 0
        for right in range(len(nums)):
            while q and q[0] < left:
                q.popleft()
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            if right >= k - 1:
                ans.append(nums[q[0]])
                left += 1
        return ans