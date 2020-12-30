# https://leetcode.com/problems/power-of-three/
from math import log10


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (log10(n) / log10(3)).is_integer() if n > 0 else False
