class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        i, j = 0, 0
        sum1, sum2 = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # nums1[i] is smaller, add it to sum1 and move i
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                # nums2[j] is smaller, add it to sum2 and move j
                sum2 += nums2[j]
                j += 1
            else:
                # Common element found - we can switch paths here
                # Take the better path up to this point, add common element
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        
        # Add remaining elements from nums1 if any
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        
        # Add remaining elements from nums2 if any
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1
        
        # Return the maximum of both paths
        return max(sum1, sum2) % MOD