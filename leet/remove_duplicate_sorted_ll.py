from operator import ne
from typing import Optional
from .common.list_node import ListNode


class Solution:
    def remove_duplicate(self, l: Optional[ListNode]):
        '''
        Remove all duplication, keep only disctinct value
        The idea is simple:
        Create another list that holds only distinct values from the original list
        This can be done by iterating the original list and keep track of the last
            non repeat values.
        Since the list is sorted, once the iteration passes a value, it never repeats
        '''
        if l is None:
            return l
        pre = l.val
        p = l.next
        t = l
        while p is not None:
            if pre != p.val:
                t.next = p
                pre = p.val
                t = t.next
            p = p.next
        t.next = None
        return l

    def remove_duplicate_delete(self, l: Optional[ListNode]):
        """
        completely delete all values that has a duplication, keep only those that are distinct 
        Args:
            l (Optional[ListNode]): the linked list

        Returns:
            Optional[ListNode]: the linked list after remove duplicate
        """
        if l is None:
            return l
        pre = ListNode(val=0, next=l)
        it = pre
        duplicate: int
        # since we need to completely remove the duplication value node,
        # we have to have a record of the previous node, by this logic
        # we can choose to monitor duplication of the next node (so we dont need
        # to keep a record of the previous node)
        while it.next is not None and it.next.next is not None:
            # duplication happens at the next node
            if it.next.val == it.next.next.val:
                duplicate = it.next.val
                # keep removing the next node until we have a node with different value than the
                # duplicate value
                while it.next is not None and it.next.val == duplicate:
                    it.next = it.next.next
            else:
                it = it.next
        return pre.next

    # I dont understand this, sorry
    def remove_duplicate_delete_recursive(self, l: Optional[ListNode]):
        # basecase one
        if l is None:
            return l
        if l.next is None:
            return l
        p = l.next
        v = l.val
        if v != p.val:
            l.next = self.remove_duplicate_delete_recursive(p)
            return l
        else:
            while p.next is not None and p.val == v:
                p = p.next
            return self.remove_duplicate_delete_recursive(p)
