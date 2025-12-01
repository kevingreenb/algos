class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array for O(log(min(n,m)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        lo, hi = 0, m
        
        while lo <= hi:
            i = (lo + hi) // 2  # partition index in nums1
            j = half - i         # partition index in nums2
            
            # Get the four boundary values (use inf for out-of-bounds)
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if partition is correct
            if left1 <= right2 and left2 <= right1:
                # Found valid partition
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1  # Move partition left in nums1
            else:
                lo = i + 1  # Move partition right in nums1
        
        return 0.0  # Should never reach here with valid input