from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None, orig = False):
        self.val = val
        self.orig = orig
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if len(node.neighbors) == 0:
            return Node(node.val)
        
        visited = {}
        cped = {}
        q = [node]
        rthead = head = Node(1)
        while len(q) > 0:
            cur = q.pop()
            if cur.val in visited:
                if len(q) > 0:
                    head = cped[q[-1].val]
                continue

            visited[cur.val] = cur
            if len(cur.neighbors) != 0:
                for n in cur.neighbors:
                    if n.val not in cped:
                        head.neighbors.append(Node(n.val))
                        cped[n.val] = head.neighbors[-1]
                    else:
                        head.neighbors.append(cped[n.val])
                    q.append(n)
            if len(q) > 0:
                head = cped[q[-1].val]
        return rthead

    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)

# if __name__ == '__main__':
#     ns = []
#     for i in range(1, 5):
#         ns.append(Node(i, orig=True))
#     ns[0].neighbors = [ns[1], ns[3]]
#     ns[1].neighbors = [ns[0], ns[2]]
#     ns[2].neighbors = [ns[1], ns[3]]
#     ns[3].neighbors = [ns[0], ns[2]]
#     s = Solution()
#     cphead = s.cloneGraph(ns[0])
#     q = [cphead]
#     q_dict = {}
#     while len(q) > 0:
#         cur = q.pop()
#         if cur.val in q_dict:
#             continue
#         q_dict[cur.val] = 1
#         if cur.orig:
#             print(cur.val)

#         for n in cur.neighbors:
#             q.append(n)