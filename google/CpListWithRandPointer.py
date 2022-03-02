"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if (head is not None):
            n_head = n_cur = Node(x=head.val)
            cp_lst = [head]
            head = head.next
            cp_lst[-1].next = n_cur
        else:
            return None
        
        while (head is not None):
            n_cur.next = Node(x=head.val)
            n_cur = n_cur.next
            cp_lst.append(head)
            head = head.next
            cp_lst[-1].next = n_cur

        cnt = 0
        n_cur = n_head
        while (n_cur is not None):
            if (cp_lst[cnt].random is not None):
                n_cur.random = cp_lst[cnt].random.next
            else:
                n_cur.random = None
            n_cur = n_cur.next
            cnt += 1
        for i in range(len(cp_lst) - 1):
            cp_lst[i].next = cp_lst[i+1]
        cp_lst[-1].next = None

        return n_head
