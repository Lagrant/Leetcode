# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tempfile import tempdir


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = None
        if (list1 is None):
            return list2
        elif (list2 is None):
            return list1
        elif (list1.val < list2.val):
            cur = list1
            list1 = list1.next
        else:
            cur = list2
            list2 = list2.next
        head = cur
        while (list1 is not None and list2 is not None):
            if (list1.val < list2.val):
                temp = list1
                list1 = list1.next
                cur.next = temp
                cur = cur.next
            else:
                temp = list2
                list2 = list2.next
                cur.next = temp
                cur = cur.next
        
        cur.next = list1 if (list1 is not None) else list2
    
        return head