from leet.zigzag_conversion import Solution


def test_base():
    s = "PAYPALISHIRING"
    num_rows = 3
    sol = Solution()
    assert sol.convert(s=s, numRows=num_rows) == "PAHNAPLSIIGYIR"


def test_alt_num_rows():
    s = "PAYPALISHIRING"
    num_rows = 4
    sol = Solution()
    assert sol.convert(s=s, numRows=num_rows) == "PINALSIGYAHRPI"


def test_num_rows_one():
    s = "kboa"
    num_row = 1
    sol = Solution()
    assert sol.convert(s=s, numRows=num_row) == s
