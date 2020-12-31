from main.reverse_integer import Solution


def test_convert():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(0) == 0
