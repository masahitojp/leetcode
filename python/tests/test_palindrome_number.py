from main.palindrome_number import Solution


def test_isPalindrome():
    assert Solution().isPalindrome(121) == True
    assert Solution().isPalindrome(-121) == False
    assert Solution().isPalindrome(10) == False
