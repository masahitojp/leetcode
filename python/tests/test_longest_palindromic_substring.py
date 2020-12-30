from main.longest_palindromic_substring import Solution


def test_longestPalindrome():
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("ac") == "a"
