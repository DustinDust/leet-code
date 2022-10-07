from leet.common.list_node import ListNode


class ListNodeUtils:
    @classmethod
    def listnode_tostring(self, l: ListNode):
        str = f'{l.val}'
        while l.next is not None:
            l = l.next
            str += f', {l.val}'
        return str

    @classmethod
    def make_list_node(self, ls: list[int]):
        res: ListNode = ListNode(val=ls[0])
        t = res
        for i in range(1, len(ls)):
            t.next = ListNode(val=ls[i])
            t = t.next
        return res
