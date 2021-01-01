import math
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        temp: str = s.lstrip()
        int_min: int = -1 * int(math.pow(2, 31))
        int_max: int = int(math.pow(2, 31)) - 1
        ans = 0
        if len(temp) > 0:
            if temp[0] == "-" or temp[0] == "+" or temp[0].isdecimal():
                if len(temp) == 1 and temp[0].isdecimal():
                    ans = int(temp)
                elif len(temp) > 1 and (
                    temp[1] != "-" and temp[1] != "+" and temp[1] != " "
                ):
                    m = re.findall(r"^-?\+?[0-9]+", temp)
                    try:
                        ans = int(m[0])
                    except:
                        ans = 0
        if ans < int_min:
            ans = int_min
        elif ans > int_max:
            ans = int_max
        return ans
