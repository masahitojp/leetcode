from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_warter: int = 0
        l, r = 0, len(height) - 1
        while l < r:
            max_warter = max(max_warter, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_warter
