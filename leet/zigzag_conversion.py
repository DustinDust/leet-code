class Solution:
    def convert(self, s: str, numRows: int):
        arr_repr: list[list[str]] = [[''] * 10 for _ in range(10)]
        '''
        First approach: keep track of 3 pointer: 
            the down pointer that go along with numRows
            the side pointer that move when down pointer hit max then reset the down pointer
            the up pointer will take care of the actual zig zag pattern by increase only one for each side step
        '''
        down, side, up = 0, 0, 0
        for c in s:
            if up == 0:
                arr_repr[down % numRows][side] = c
                down += 1
                if down % numRows == 0 and down != 0:
                    up = down - 1
                    down = 0
                    side += 1
            else:
                up -= 1
                if up == 0:
                    down += 1
                arr_repr[up][side] = c
                if up != 0:
                    side += 1
        res = ''
        for i in arr_repr:
            for j in i:
                if j != '':
                    res += j
        return res
