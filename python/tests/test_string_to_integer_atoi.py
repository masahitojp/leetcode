from main.string_to_integer_atoi import Solution


def test_myAtoi():
    assert Solution().myAtoi("42") == 42
    assert Solution().myAtoi("   -42") == -42
    assert Solution().myAtoi("4193 with words") == 4193
    assert Solution().myAtoi("words and 987") == 0
    assert Solution().myAtoi("-91283472332") == -2147483648
    assert Solution().myAtoi("3.14159") == 3
    assert Solution().myAtoi("1") == 1
    assert Solution().myAtoi("+1") == 1
    assert Solution().myAtoi("1a") == 1
    assert Solution().myAtoi("-+12") == 0
