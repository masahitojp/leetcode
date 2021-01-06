from main.regular_expression_matching import Solution


def test_isPowerOfThree():
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True
    assert Solution().isMatch(s="mississippi", p="mis*is*p*.") == False
    assert Solution().isMatch(s="mississippi", p="mis*is*ip*.") == True
    assert Solution().isMatch("abcd", "d*") == False
    assert Solution().isMatch("aaa", "a.a") == True
    assert Solution().isMatch("aaa", "ab*a") == False
    assert Solution().isMatch("aaa", "ab*ac*a") == True
    # assert Solution().isMatch("aaa", "ab*a*c*a") == True
