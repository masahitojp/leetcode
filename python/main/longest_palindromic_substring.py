class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans, len_ans, len_s = s[0], 1, len(s)

        for i in range(len_s):
            for j in range(i + len_ans + 1, len_s + 1):
                sub = s[i:j]
                if sub == sub[::-1]:  # check parindrome
                    ans, len_ans = sub, len(sub)
        return ans
