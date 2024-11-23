from typing import List
from collections import defaultdict, deque
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = defaultdict(list)
        res = []
        for acc in accounts:
            users[acc[0]].append(acc[1:])
        for user, emails in users.items():
            graph = {}
            for i in range(len(emails)):
                for e in emails[i]:
                    if e not in graph:
                        graph[e] = set(emails[i])
                    else:
                        graph[e].update(emails[i])
            for g in graph:
                graph[g] = list(graph[g])
            while len(graph.keys()) > 0:
                for g in graph:
                    indiv = self.connected_components(graph, g)
                    if len(indiv) > 0:
                        res.append([user] + sorted(indiv))
                    break
        return res
            
    def connected_components(self, graph, start):
        visited = {}
        que = deque([start])
        while len(que) > 0:
            cur = que.popleft()
            if cur in visited:
                continue
            visited[cur] = True
            for adj in graph[cur]:
                if adj not in visited:
                    visited[adj] = True
                    que.extend(graph[adj])
        for v in visited:
            if v in graph:
                del graph[v]
        return list(visited.keys())
    
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            x = self.par[x]
            self.par[x] = self.par[self.par[x]]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailToGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailToGroup[leader].append(e)
        
        res = []

        for i, email in emailToGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailToGroup[i]))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))