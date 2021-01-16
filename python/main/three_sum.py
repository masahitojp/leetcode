from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n: int = len(nums)
        ans: List[List[int]] = []
        if n == 0:
            return ans
        nums.sort()
        for i in range(n):
            lp: int = i + 1
            rp: int = n - 1
            while lp < rp:
                total_sum: int = nums[i] + nums[lp] + nums[rp]
                if total_sum == 0:
                    temp: List[int] = [nums[i], nums[lp], nums[rp]]
                    if not (temp in ans):
                        ans.append(temp)
                    l_num: int = nums[lp]
                    while lp < n - 1 and l_num == nums[lp]:
                        lp += 1

                    r_num: int = nums[rp]
                    while lp < rp and nums[rp] == r_num:
                        rp -= 1
                elif total_sum > 0:
                    rp -= 1
                else:
                    lp += 1

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1

        return ans
