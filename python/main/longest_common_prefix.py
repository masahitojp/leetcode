from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs = len(strs)
        if len_strs == 0:
            return ""
        elif len_strs == 1:
            return strs[0]
        else:
            first = strs[0]
            ans: str = ""
            for i in range(1, len(first) + 1):
                for j in range(1, len_strs):
                    print(i, strs[j][:i], first[:i])
                    if strs[j][:i] != first[:i]:
                        print("ees")
                        return ans
                    else:
                        pass
                ans = first[:i]
            return ans
