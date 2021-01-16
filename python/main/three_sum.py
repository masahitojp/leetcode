from typing import List, Set


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        ans: List[List[int]] = []
        if n < 3:
            return ans
        nums.sort()
        pair: Set[int] = set()
        for i in range(n):
            lp: int = i + 1
            rp: int = n - 1
            while lp < rp:
                total_sum: int = nums[i] + nums[lp] + nums[rp]
                if total_sum == 0:
                    if not ((nums[i], nums[lp]) in pair):
                        ans.append([nums[i], nums[lp], nums[rp]])
                        pair.add((nums[i], nums[lp]))
                    lp += 1
                    rp -= 1
                elif total_sum > 0:
                    rp -= 1
                else:
                    lp += 1

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1

        return ans
