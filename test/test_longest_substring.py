from leet.longest_substring import Solution, SolutionFaster


def test_base():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3


def test_one_character():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("bbbbbb") == 1


def test_random():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("pwwkew") == 3


def test_faster():
    sol = SolutionFaster()
    assert sol.lengthOfLongestSubstring(s="abcabcbb") == 3
