# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)
#         while len(nums) > k:
#             heapq.heappop(nums)
#         return nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        for num in nums:
            if len(temp) == k:
                heapq.heappushpop(temp,num)
            else:
                heapq.heappush(temp,num)
        return temp[0]