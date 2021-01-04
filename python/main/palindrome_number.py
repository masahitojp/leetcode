# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y: int = x
            temp: int = 0
            while True:
                temp = temp * 10 + y % 10
                y = y // 10
                if y == 0:
                    break
            return True if temp == x else False
