from main.three_sum_closest import Solution


def test_threeSum():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([1, 1, 1, 0], -100) == 2
