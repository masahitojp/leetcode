from main.longest_common_prefix import Solution


def test_longestCommonPrefix():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert (
        Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"])
        == "flower"
    )
