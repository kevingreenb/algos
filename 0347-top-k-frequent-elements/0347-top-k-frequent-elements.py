class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        ans = []
        for num, count in counter.items():
            buckets[count].append(num)
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans