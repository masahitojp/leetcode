class Solution:
    def intToRoman(self, num: int) -> str:
        units = {
            1000: "M",
            100: "C",
            10: "X",
            1: "I",
        }
        five_units = {100: "D", 10: "L", 1: "V"}
        ans = ""
        temp = num
        for key in units:
            a = temp // key
            temp = temp % key
            if a == 4:
                ans += units[key] + five_units[key]
            elif a == 9:
                ans += units[key] + units[key * 10]
            elif a >= 5:
                ans += five_units[key] + (a % 5) * units[key]
            else:
                ans += a * units[key]
        return ans
