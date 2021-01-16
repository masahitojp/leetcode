from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans: List[List[int]] = []
        pairs: Set[int] = set()
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lp: int = i + 1
            rp: int = n - 1
            while lp < rp:

                total_sum: int = nums[i] + nums[lp] + nums[rp]
                if total_sum == 0:
                    pair: Tuple[int, int] = (nums[i], nums[lp])
                    if not (pair in pairs):
                        ans.append([nums[i], nums[lp], nums[rp]])
                        pairs.add(pair)
                    lp += 1
                    rp -= 1
                elif total_sum > 0:
                    rp -= 1
                else:
                    lp += 1

        return ans
