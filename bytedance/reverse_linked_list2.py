from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        mid = (left + right + 1) // 2 # < mid
        i = 1
        stack1, stack2 = [], []
        cur = head
        left_prev, mid_node = None, None
        while i <= right:
            if i < left - 1:
                cur = cur.next_
                i += 1
                continue
            elif i == left - 1:
                left_prev = cur
                cur = cur.next_
                i += 1
                continue
            if i < mid:
                stack1.append(cur)
            elif i == mid:
                if mid != (left + right) / 2:
                    stack2.append(cur)
                else:
                    mid_node = cur
            else:
                stack2.append(cur)
            cur = cur.next_
            i += 1
        if left == 1:
            head = left_prev = stack2[-1]
            stack2 = stack2[:-1]
        for i in range(len(stack2) - 1, -1, -1):
            left_prev.next_ = stack2[i]
            left_prev = left_prev.next_
        if mid == (left + right) / 2:
            left_prev.next_ = mid_node
            left_prev = left_prev.next_
        for i in range(len(stack1) - 1, -1, -1):
            left_prev.next_ = stack1[i]
            left_prev = left_prev.next_
        left_prev.next_ = cur
        return head
    
if __name__ == '__main__':
    s = Solution()
    cur1 = head1 = ListNode(1)
    for j in range(2, 3):
        head1.next_ = ListNode(j)
        head1 = head1.next_
    s.reverseBetween(cur1, 1, 2)