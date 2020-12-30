class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans: list[str] = ["" for i in range(numRows)]
        len_s: int = len(s)
        cycle: int = numRows * 2 - 2

        for i in range(len_s):
            z = i % cycle
            if numRows <= z < cycle:
                z = cycle - z
            ans[z] += s[i]

        return "".join(ans)
