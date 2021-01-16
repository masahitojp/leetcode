from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        ans = []
        if len_nums < 3:
            return []
        for i in range(len_nums - 2):
            for j in range(i + 1, len_nums - 1):
                for k in range(j + 1, len_nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        if not (temp in ans):
                            ans.append(temp)
        print(ans)
        return ans
