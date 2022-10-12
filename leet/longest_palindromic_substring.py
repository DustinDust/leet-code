class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''Bruteforce'''
        def is_palindrome(l, r, s: str) -> bool:
            for i in range(l, r + 1):
                if s[i] != s[l + r - i]:
                    return False
            return True

        if len(s) == 1:
            return s
        max_len = 0
        res = (0, 0)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(i, j, s):
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        res = (i, j + 1)
        return s[res[0]:res[1]]


class SolutionFast:
    def __init__(self) -> None:
        self.palindrome_table: list[list[bool]] = [
            [None] * 1000 for i in range(1000)]

    def longestPalindrome(self, s: str) -> str:
        '''Still not fast enough D:'''
        if s[::-1] == s:
            return s

        def dp_palindrome_check(i, j) -> bool:
            if i < 0 or j >= len(s):
                return False
            if i == j:
                return True
            if j == i + 1:
                return s[i] == s[j]
            if self.palindrome_table[i][j] is not None:
                return self.palindrome_table[i][j]
            else:
                self.palindrome_table[i][j] = dp_palindrome_check(
                    i + 1, j - 1) and s[i] == s[j]
                return self.palindrome_table[i][j]

        res = (0, 0)
        maxlen = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                is_palindrome = dp_palindrome_check(i, j)
                if is_palindrome:
                    if j - i + 1 > maxlen:
                        res = (i, j + 1)
                        maxlen = max(maxlen, j-i+1)

        return s[res[0]:res[1]]


class SolutionFaster:
    def longestPalindrome(self, s: str) -> str:
        '''
        Used the idea of expanding palindrome from the middle to reduce the time required for looping
        through substring. We only loop each character once, consider it a middle point for a palindrome
        then start expanding to the 2 other side of the string until the expanded string is no longer a palindrome

        O(n) for a loop through each character, O(n) for finding the longest palidrome with that character as a middle point
            => O(n^2) time complexity and O(1) space complexity

        There's a case where the palindrome is even e.g "aa", we handle that using 2 pointers. 
        Overall 2 pointers is much cleaner than only using one "distance from middle point" variables
        '''
        res = (0, 1)
        maxlen = 0
        for i in range(len(s)):
            # l and r are the 2 pointers
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = (l, r + 1)
                    maxlen = r-l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    res = (l, r + 1)
                    maxlen = r-l+1
                l -= 1
                r += 1

        return s[res[0]:res[1]]

        """
        Another great solution using Dynamic programming (tabulation) (better one that i implemented my own ;-;)
        https://leetcode.com/problems/longest-palindromic-substring/solutions/151144/bottom-up-dp-two-pointers/
        """
