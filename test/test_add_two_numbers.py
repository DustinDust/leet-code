from leet.add_two_numbers import Solution, ListNode
from leet.utils.list_node_utils import ListNodeUtils
import pytest


@pytest.fixture
def sol():
    return Solution()


def test_base(sol):
    l1 = ListNodeUtils.make_list_node([2, 4, 3])
    l2 = ListNodeUtils.make_list_node([5, 6, 4])
    res_sample = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))
    res = sol.add_two_numbers(l1, l2)
    assert ListNodeUtils.listnode_tostring(
        l=res) == ListNodeUtils.listnode_tostring(l=res_sample)


def test_zero_list(sol):
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    res_sample = ListNode(val=0)
    res = sol.add_two_numbers(l1, l2)
    assert ListNodeUtils.listnode_tostring(
        l=res) == ListNodeUtils.listnode_tostring(l=res_sample)


def test_dif_size_list(sol):
    l1 = ListNodeUtils.make_list_node([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNodeUtils.make_list_node([9, 9, 9, 9])
    res_sample = ListNodeUtils.make_list_node([8, 9, 9, 9, 0, 0, 0, 1])
    res = sol.add_two_numbers(l1, l2)
    assert ListNodeUtils.listnode_tostring(
        l=res) == ListNodeUtils.listnode_tostring(l=res_sample)
