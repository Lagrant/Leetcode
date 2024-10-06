"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next_: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next_ = next_
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        
        cur = cphead = Node(head.val)
        rd_lst = []
        cprd_lst = []
        while head.next_ is not None:
            rdptr = head
            rd_lst.append(rdptr)
            cpptr = cur
            cprd_lst.append(cpptr)

            cur.next_ = Node(head.next_.val)
            cur = cur.next_
            head = head.next_
        rd_lst.append(head)
        cprd_lst.append(cur)
        for rd1, cp1 in zip(rd_lst, cprd_lst):
            if rd1.random is None:
                continue
            for rd2, cp2 in zip(rd_lst, cprd_lst):
                if rd1.random == rd2:
                    cp1.random = cp2
        return cphead
