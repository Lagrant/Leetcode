from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        piv = len(lists) // 2
        nodei = self.mergeKLists(lists[:piv])
        nodej = self.mergeKLists(lists[piv:])
        if nodei is None:
            return nodej
        if nodej is None:
            return nodei
        if nodei.val <= nodej.val:
            head = m_list = nodei
            nodei = nodei.next
        else:
            head = m_list = nodej
            nodej = nodej.next
        while nodei is not None and nodej is not None:
            if nodei.val <= nodej.val:
                m_list.next = nodei
                m_list = m_list.next
                nodei = nodei.next
            else:
                m_list.next = nodej
                m_list = m_list.next
                nodej = nodej.next
        if nodei is not None:
            m_list.next = nodei
        if nodej is not None:
            m_list.next = nodej
        return head