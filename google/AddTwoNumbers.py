# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = sum_lst = ListNode(l1.val + l2.val + carry)
        l1 = l1.next
        l2 = l2.next
        if (sum_lst.val > 9):
            sum_lst.val -= 10
            carry = 1
        while (l1 is not None and l2 is not None):
            sum_lst.next = ListNode()
            sum_lst = sum_lst.next
            sum_lst.val = l1.val + l2.val + carry
            if (sum_lst.val > 9):
                sum_lst.val -= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next

        if (l1 is None and l2 is None):
            if (carry == 1):
                sum_lst.next = ListNode(1)
        else:
            l = l1 if (l1 is not None) else l2
            while (l is not None):
                sum_lst.next = ListNode(carry + l.val)
                sum_lst = sum_lst.next
                if (sum_lst.val > 9):
                    sum_lst.val -= 10
                    carry = 1
                else:
                    carry = 0
                l = l.next
        if (carry == 1):
            sum_lst.next = ListNode(1)
        
        return head

