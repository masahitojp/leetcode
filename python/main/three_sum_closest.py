from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        diff: int = 2 ** 31 - 1
        nums.sort()
        for i in range(n):
            lp: int = i + 1
            rp: int = n - 1
            while lp < rp:

                total_sum: int = nums[i] + nums[lp] + nums[rp]
                if abs(target - total_sum) < abs(diff):
                    diff = target - total_sum
                elif total_sum < target:
                    lp += 1
                else:
                    rp -= 1
            if diff == 0:
                break

        return target - diff
