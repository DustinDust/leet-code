from leet.add_two_numbers import Solution, ListNode


def make_list_node(ls: list[int]):
    res: ListNode = ListNode(val=ls[0])
    t = res
    for i in range(1, len(ls)):
        t.next = ListNode(val=ls[i])
        t = t.next
    return res


def test_make_list_node():
    l1 = make_list_node([2, 4, 3])
    l2 = make_list_node([5, 6, 4])
    l1r = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2r = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    sol = Solution()
    assert sol.listnode_tostring(l1) == sol.listnode_tostring(l1r)
    assert sol.listnode_tostring(l2) == sol.listnode_tostring(l2r)


def test_base():
    l1 = make_list_node([2, 4, 3])
    l2 = make_list_node([5, 6, 4])
    # l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    # l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    sol = Solution()
    res_sample = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8)))
    res = sol.add_two_numbers(l1, l2)
    assert sol.listnode_tostring(l=res) == sol.listnode_tostring(l=res_sample)


def test_zero_list():
    l1 = ListNode(val=0)
    l2 = ListNode(val=0)
    sol = Solution()
    res_sample = ListNode(val=0)
    res = sol.add_two_numbers(l1, l2)
    assert sol.listnode_tostring(l=res) == sol.listnode_tostring(l=res_sample)


def test_dif_size_list():
    l1 = make_list_node([9, 9, 9, 9, 9, 9, 9])
    l2 = make_list_node([9, 9, 9, 9])
    sol = Solution()
    res_sample = make_list_node([8, 9, 9, 9, 0, 0, 0, 1])
    res = sol.add_two_numbers(l1, l2)
    assert sol.listnode_tostring(res) == sol.listnode_tostring(res_sample)
