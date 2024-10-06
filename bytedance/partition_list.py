from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next_ is None:
            return head
        cur = head
        start, prev = None, None
        # appro = 101
        while cur is not None and cur.val < x:
            start = cur
            prev = cur
            cur = cur.next_
        if cur is None:
            return head
        while cur is not None:
            if cur.val >= x:
                prev = cur
                cur = cur.next_
            else:
                if start is None:
                    start = cur
                    if prev is not None:
                        prev.next_ = cur.next_
                    start.next_ = head
                    head = start
                    if prev is not None:
                        cur = prev.next_
                else:
                    prev.next_ = cur.next_
                    cur.next_ = start.next_
                    start.next_ = cur
                    start = cur
                    cur = prev.next_
        return head

if __name__ == '__main__':
    s = Solution()
    cur1 = head1 = ListNode(1)
    lst = [1]
    for i in lst:
        head1.next_ = ListNode(i)
        head1 = head1.next_
    s.partition(cur1, 2)