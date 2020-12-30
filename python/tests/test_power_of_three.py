from main.power_of_three import Solution


def test_isPowerOfThree():
    assert Solution().isPowerOfThree(1) == True
    assert Solution().isPowerOfThree(0) == False
    assert Solution().isPowerOfThree(27) == True
    assert Solution().isPowerOfThree(-3) == False
