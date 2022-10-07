from leet.common.list_node import ListNode
from leet.utils.list_node_utils import ListNodeUtils


def test_make_list_node():
    l1 = ListNodeUtils.make_list_node([2, 4, 3])
    l2 = ListNodeUtils.make_list_node([5, 6, 4])
    l1r = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2r = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    assert ListNodeUtils.listnode_tostring(
        l1) == ListNodeUtils.listnode_tostring(l1r)
    assert ListNodeUtils.listnode_tostring(
        l2) == ListNodeUtils.listnode_tostring(l2r)
