from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        cnt = 0
        if k == 1 or head.next_ is None:
            return head
        prev = None
        while cur is not None and cur.next_ is not None:
            stack = []
            while cnt < k and cur is not None:
                stack.append(cur)
                cur = cur.next_
                cnt += 1
            if cur is None and cnt < k:
                return head
            stack[0].next_ = stack[-1].next_
            for i in range(len(stack) -1):
                stack[i + 1].next_ = stack[i]
            if prev is not None:
                prev.next_ = stack[-1]
            else:
                head = stack[-1]
            prev = stack[0]
            cur = prev.next_
            cnt = 0
        return head