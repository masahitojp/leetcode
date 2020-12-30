# for leetcode
# https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = sorted(nums1 + nums2)
        l = len(c)
        ans = 0
        if l % 2 == 1:
            ans = c[l // 2]
        else:

            ans = (c[l // 2 - 1] + c[l // 2]) / 2
        return ans
