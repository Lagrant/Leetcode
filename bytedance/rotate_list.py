from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k == 0 or head.next_ is None:
            return head
        
        cur = head
        cnt = 1
        rthead = None
        rtprev = None
        prev = None
        while cur is not None:
            if cnt == k:
                rthead = head
            elif cnt > k:
                rtprev = rthead
                rthead = rthead.next_
            prev = cur
            cur = cur.next_
            cnt += 1
        cnt -= 1
        
        if rthead is not None:
            if rtprev is None:
                return head
            else:
                rtprev.next_ = None
                prev.next_ = head
                return rthead
        else:
            k %= cnt
            if k == 0:
                return head
            k = cnt - k
            c = 1
            cur2 = head
            while c < k:
                cur2 = cur2.next_
                c += 1
            newhead = cur2.next_
            cur2.next_ = None
            prev.next_ = head
            return newhead

if __name__ == '__main__':
    s = Solution()
    cur1 = head1 = ListNode(1)
    for j in range(2, 6):
        head1.next_ = ListNode(j)
        head1 = head1.next_
    s.rotateRight(cur1, 10)