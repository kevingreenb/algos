class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]


        def rob_linear(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            prev2 = houses[0]
            prev1 = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                current = max(prev2 + houses[i], prev1)
                prev2 = prev1
                prev1 = current
                
            return prev1
        
        # We run your logic twice: 
        # once excluding the last house, once excluding the first.
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
