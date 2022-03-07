import collections
import itertools
class Solution:
    """
    Hierholzer algorithm
    """
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join([str(i) for i in range(k)])
        
        #build the digraph
        nodeLists = itertools.product([str(i) for i in range(k)], repeat=n-1)
        nodes = [''.join(nodeList) for nodeList in nodeLists]
        neighbors = {}
        for node in nodes:
            neighbors[node] = {node[1:] + str(i) for i in range(k)}
        
        #Hierholzer's algorithm for Eulerian circuit in Eulerian digraph
        start = '0' * (n-1)
        deque = collections.deque([start])
        i = -1
        while i != len(deque) - 1:
            curr_node = deque[-1]
            if neighbors[curr_node]:
                next_node = neighbors[curr_node].pop()
                deque.append(next_node)
            else:
                if i != -1:
                    deque.rotate(1)
                else:
                    deque.pop()
                i += 1
        
        return start + ''.join(node[-1] for node in deque)

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = list()
        nodeNum = k**(n-1)
        edges = [k-1]*nodeNum

        node = 0
        while edges[node] >= 0:
            edge = edges[node]
            edges[node] -= 1
            node = (node * k + edge) % nodeNum
            ans.append(str(edge))
    
        return  "0"*(n-1)  + "".join(ans)