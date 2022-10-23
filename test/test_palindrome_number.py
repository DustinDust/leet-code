from leet.palindrome_number import Solution


def test_base():
    input = 121
    sol = Solution()
    res = sol.isPalindrome(input)
    assert res == True


def test_negative():
    input = -121
    sol = Solution()
    res = sol.isPalindrome(input)
    assert res == False


def test_alt():
    input = 10
    sol = Solution()
    res = sol.isPalindrome(input)
    assert res == False
