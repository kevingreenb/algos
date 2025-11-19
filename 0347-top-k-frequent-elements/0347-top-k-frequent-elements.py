class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, v in d.items():
            buckets[v].append(key)

        ans = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                if len(ans) == k:
                    return ans
                ans.append(num)
        
        return ans


        