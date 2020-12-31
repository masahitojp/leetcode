from math import pow


class Solution:
    def reverse(self, x: int) -> int:
        ans: int = 0
        y = 1 if x >= 0 else -1
        z = y * x
        while True:
            ans = ans * 10 + z % 10
            if z // 10 != 0:
                z = z // 10
            else:
                break
        ans = y * ans
        if ans < (-1 * pow(2, 31)) or ans > (pow(2, 31) - 1):
            return 0
        else:
            return ans
