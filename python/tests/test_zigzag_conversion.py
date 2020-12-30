from main.zigzag_conversion import Solution


def test_convert():
    assert Solution().convert("A", 1) == "A"
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
