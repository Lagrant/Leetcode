from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next_ is None:
            return head
        
        cur = head
        prev = None
        dup_dict = {}
        while cur is not None and cur.next_ is not None:
            if cur.val not in dup_dict and cur.val == cur.next_.val:
                dup_dict[cur.val] = True
            if prev is None:
                if cur.val in dup_dict:
                    head = cur.next_
                else:
                    prev = head
            else:
                if cur.val in dup_dict:
                    prev.next_ = cur.next_
                else:
                    prev.next_ = cur
                    prev = prev.next_
            cur = cur.next_
        if prev is None:
            return None if cur.val in dup_dict else head
        else:
            prev.next_ = None if cur.val in dup_dict else cur
                
        return head
    
if __name__ == '__main__':
    s = Solution()
    cur1 = head1 = ListNode(1)
    for j in range(1, 3):
        head1.next_ = ListNode(j)
        head1 = head1.next_
    s.deleteDuplicates(cur1)