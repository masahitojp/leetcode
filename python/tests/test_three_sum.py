from main.three_sum import Solution


def test_threeSum():
    actual = Solution().threeSum(
        [-1, 0, 1, 2, -1, -4],
    )
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert {(frozenset(item)) for item in actual} == {
        (frozenset(item)) for item in expected
    }
