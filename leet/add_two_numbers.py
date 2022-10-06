from distutils.command.build_scripts import first_line_re
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def listnode_tostring(self, l: ListNode):
        str = f'{l.val}'
        while l.next is not None:
            l = l.next
            str += f', {l.val}'
        return str

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_v = l1.val + l2.val if l1 is not None and l2 is not None else 0
        r_digit = 0
        if first_v >= 10:
            first_v = first_v % 10
            r_digit = 1
        res = ListNode(val=first_v)
        t = res
        t1, t2 = l1.next, l2.next
        while t1 != None or t2 != None:
            v1 = 0
            v2 = 0
            if t1 != None:
                v1 = t1.val
            if t2 != None:
                v2 = t2.val
            cur_val = v1 + v2 + r_digit
            r_digit = 0
            if cur_val >= 10:
                r_digit = 1
                cur_val = cur_val % 10
            t.next = ListNode(val=cur_val)
            t = t.next
            t1 = t1.next if t1 != None else None
            t2 = t2.next if t2 != None else None
        if r_digit > 0:
            t.next = ListNode(val=r_digit)
        return res
