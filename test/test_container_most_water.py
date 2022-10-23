from leet.container_most_water import Solution


def test_base():
    input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    res = sol.maxArea(input)
    assert res == 49
    res = sol.maxArea_2Pointer(input)
    assert res == 49


def test_edge():
    input = [1, 1]
    sol = Solution()
    res = sol.maxArea(input)
    assert res == 1
    res = sol.maxArea_2Pointer(input)
    assert res == 1
