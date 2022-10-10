from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Bruteforce approach, check every single substring, make sure its not repeating'''
        ts = ''
        max_len = 0
        l = 0
        start = 0
        while start < len(s):
            for i in range(start, len(s)):
                if s[i] not in ts:
                    max_len = max(l + 1, max_len)
                    l += 1
                    ts += s[i]
                else:
                    start += 1
                    l = 0
                    ts = ''
                    break
        return max_len


class SolutionFaster:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Faster approach. The idea is the same as before, but the subproblem of 
        checking a non-repeating substring is improved by using set'''
        cset = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[i])
            res = max(res, i - l + 1)
        return res
