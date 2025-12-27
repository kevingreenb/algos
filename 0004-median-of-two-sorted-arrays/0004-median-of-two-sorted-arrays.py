class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1 switch
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # 2 set variables
        m, n = len(nums1), len(nums2)
        total = m + n 
        half = total // 2
        l, r = 0, m

        # 3 loop binary search
        while l <= r:
            i = (l + r) // 2
            j = half - i

            # 4 divide nums1 in 2
            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            # 5 divide nums2 in 2
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # 6 find a match 
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                return (max(left1, left2)+min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
        return 0.0
        