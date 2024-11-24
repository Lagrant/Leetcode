"""
# Definition for a Node.
"""
from typing import Optional
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
    
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return None

        copy_node = {} # old : new 
        copy_node[head] = Node(head.val)

        current = head 

        while current :
            if current.next and current.next not in copy_node:
                copy_node[current.next] = Node(current.next.val)
            
            copy_node[current].next = copy_node.get(current.next, None)  

            if current.random and current.random not in copy_node:
                copy_node[current.random] = Node(current.random.val)
            
            copy_node[current].random = copy_node.get(current.random, None)

            current = current.next
        
        return copy_node[head]
