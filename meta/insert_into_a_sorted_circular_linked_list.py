from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        root = head
        prev = head
        if not head:
            n1 = Node(insertVal)
            n1.next = n1
            return n1
        head = head.next
        if prev == head:
            prev.next = Node(insertVal)
            prev.next.next = prev
            return root
        cur = head
        init = True
        while head != cur or head == cur and init:
            init = False
            if head.val >= insertVal >= prev.val or (insertVal >= prev.val or insertVal < head.val) and head.val < prev.val:
                newnode = Node(insertVal, head)
                prev.next = newnode
                return root
            prev = head
            head = head.next

        newnode = Node(insertVal, head)
        prev.next = newnode
        return root
    
if __name__ == '__main__':
    node3 = Node(3)
    node4 = Node(3)
    node1 = Node(5)
    node3.next = node4
    node4.next = node1
    node1.next = node3
    s = Solution()
    print(s.insert(node4, 0))