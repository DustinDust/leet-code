
class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''Brute approach: O(n^2)'''
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area

    def maxArea_2Pointer(self, height: list[int]) -> int:
        '''Better'''
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            hl, hr = height[l], height[r]
            max_area = max((r - l) * min(hr, hl), max_area)
            if hl > hr:
                r -= 1
            else:
                l += 1
        return max_area
