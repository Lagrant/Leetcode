from collections import defaultdict
class Solution:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def calcEquation(self, equations, values, queries):
        
        for i, (eqi, eqj) in enumerate(equations):
            self.graph[eqi].append([eqj, values[i]])
            self.graph[eqj].append([eqi, 1 / values[i]])
        
        ans = []
        for (qi, qj) in queries:
            v = self.dfs(qi, {}, qj)
            ans.append(-1 if v is None else v)
        return ans
    
    def dfs(self, q, visited, e):
        for (q1, v) in self.graph[q]:
            if q1 == e:
                return v
            if q1 not in visited:
                visited[q1] = True
                res = self.dfs(q1, visited, e)
                if res is not None:
                    return v * res
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.calcEquation([["a","b"],["b","c"]], [2.0, 3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))