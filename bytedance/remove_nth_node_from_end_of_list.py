# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next_ is None:
            return None
        cnt = 0
        cur = head
        rmhead = None
        rmprev = None
        while cur is not None:
            if cnt == n - 1:
                rmhead = head
            cnt += 1
            cur = cur.next_
            if cnt > n:
                rmprev = rmhead
                rmhead = rmhead.next_
        if rmprev is None:
            return rmhead.next_
        rmprev.next_ = rmhead.next_ if rmhead is not None else None
        return head

if __name__ == '__main__':
    s = Solution()
    cur1 = head1 = ListNode(1)
    for j in range(2, 6):
        head1.next_ = ListNode(j)
        head1 = head1.next_
    s.removeNthFromEnd(cur1, 2)