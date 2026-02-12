class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        ans = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) >= k:
                    return ans
        return ans