from main.integer_to_roman import Solution


def test_intToRoman():
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(9) == "IX"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(90) == "XC"
    assert Solution().intToRoman(1994) == "MCMXCIV"
    assert Solution().intToRoman(15) == "XV"
    assert Solution().intToRoman(400) == "CD"
