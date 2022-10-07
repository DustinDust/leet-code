from leet.remove_duplicate_sorted_ll import Solution
from leet.utils.list_node_utils import ListNodeUtils as util
import pytest


@pytest.fixture(scope='session')
def solution_fixture():
    return Solution()


def test_base(solution_fixture):
    l = util.make_list_node([1, 1, 2])
    lsr = util.make_list_node([1, 2])
    lr = solution_fixture.remove_duplicate(l=l)
    assert util.listnode_tostring(lsr) == util.listnode_tostring(lr)


def test_multiple_duplication(solution_fixture):
    l = util.make_list_node([1, 1, 2, 2, 3, 3])
    lsr = util.make_list_node([1, 2, 3])
    lr = solution_fixture.remove_duplicate(l=l)
    assert util.listnode_tostring(lsr) == util.listnode_tostring(lr)


def test_delete(solution_fixture):
    l = util.make_list_node([1, 2, 3, 3, 4, 4, 5])
    lsr = util.make_list_node([1, 2, 5])
    lr = solution_fixture.remove_duplicate_delete(l=l)
    assert util.listnode_tostring(lsr) == util.listnode_tostring(lr)


def test_delete_duplication_first_node(solution_fixture):
    l = util.make_list_node([1, 1, 1, 2, 3])
    lsr = util.make_list_node([2, 3])
    lr = solution_fixture.remove_duplicate_delete(l=l)
    assert util.listnode_tostring(lsr) == util.listnode_tostring(lr)
