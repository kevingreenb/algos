class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            # Find the index of the first element >= x
            idx = bisect.bisect_left(tails, x)
            
            # If x is larger than any element in tails, extend the list
            if idx == len(tails):
                tails.append(x)
            # Otherwise, replace the element at idx with x to keep tails small
            else:
                tails[idx] = x
                
        return len(tails)