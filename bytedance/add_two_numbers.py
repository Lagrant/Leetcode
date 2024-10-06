class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = res_list = ListNode(0)
        prev = head
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + res_list.val
            if val > 9:
                res_list.val = val - 10
                next_ = ListNode(1)
            else:
                res_list.val = val
                next_ = ListNode(0)
            l1 = l1.next_
            l2 = l2.next_
            res_list.next_ = next_
            prev = res_list
            res_list = next_
        
        ll = l1 if l1 is not None else l2
        while ll is not None:
            val = ll.val + res_list.val
            if val > 9:
                res_list.val = val % 10
                next_ = ListNode(val // 10)
                res_list.next_ = next_
                prev = res_list
                res_list = next_
                ll = ll.next_
            else:
                res_list.val = val
                ll = ll.next_
                if ll is not None:
                    next_ = ListNode(0)
                    res_list.next_ = next_
                    prev = res_list
                    res_list = next_
                else:
                    break
        if res_list.val == 0:
            prev.next_ = None
        return head
    

    def addTwoNumbers2(self, l1, l2):
        carry = 0
        head = sum_lst = ListNode(l1.val + l2.val + carry)
        l1 = l1.next_
        l2 = l2.next_
        if (sum_lst.val > 9):
            sum_lst.val -= 10
            carry = 1
        while (l1 is not None and l2 is not None):
            sum_lst.next_ = ListNode()
            sum_lst = sum_lst.next_
            sum_lst.val = l1.val + l2.val + carry
            if (sum_lst.val > 9):
                sum_lst.val -= 10
                carry = 1
            else:
                carry = 0
            l1 = l1.next_
            l2 = l2.next_

        if (l1 is None and l2 is None):
            if (carry == 1):
                sum_lst.next_ = ListNode(1)
        else:
            l = l1 if (l1 is not None) else l2
            while (l is not None):
                sum_lst.next_ = ListNode(carry + l.val)
                sum_lst = sum_lst.next_
                if (sum_lst.val > 9):
                    sum_lst.val -= 10
                    carry = 1
                else:
                    carry = 0
                l = l.next_
        if (carry == 1):
            sum_lst.next_ = ListNode(1)
        
        return head