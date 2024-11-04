# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pcur = p
        qcur = q
        visitedp = {p.val: p}
        visitedq = {q.val: q}
        while pcur is not None or qcur is not None:
            if pcur is not None:
                visitedp[pcur.val] = pcur
            if qcur is not None:
                visitedq[qcur.val] = qcur
            if pcur is not None and qcur is not None and pcur.val == qcur.val or pcur is not None and pcur.val in visitedq:
                return pcur
            if qcur is not None and qcur.val in visitedp:
                return qcur
            if pcur is not None:
                pcur = pcur.parent
            if qcur is not None:
                qcur = qcur.parent
        
