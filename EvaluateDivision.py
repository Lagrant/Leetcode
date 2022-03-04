from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations, values, queries):
        var_graph = defaultdict(list)
        ans = []
        
        for i, var in enumerate(equations):
            var_graph[var[0]].append([var[1], values[i]])
            if (values[i] == 0):
                var_graph[var[1]].append([var[0], float('inf')])
            else:
                var_graph[var[1]].append([var[0], float(1/values[i])])
        
        for query in queries:
            equa = deque([[query[0], 1.]])
            find = False
            visited = defaultdict(bool)
            while (len(equa) > 0):
                cur = equa.popleft()
                if (len(var_graph[cur[0]]) > 0):
                    
                    for var in var_graph[cur[0]]:
                        if (var[0] == query[1]):
                            ans.append(cur[1] * var[1])
                            find = True
                            break
                        elif (not visited[var[0]]):
                            equa.append([var[0], var[1] * cur[1]])
                            visited[var[0]] = True
                    if (find):
                        break
            if (not find):
                ans.append(-1.)
        
        return ans

sol = Solution()
print(sol.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]))