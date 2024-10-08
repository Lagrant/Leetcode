from typing import List
from collections import defaultdict, deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dist = self.compare(startGene, endGene)
        if dist > len(bank):
            return -1
        if len(bank) == 1:
            if endGene == bank[0] and self.compare(startGene, endGene) == 1:
                return 1
        
        graph = defaultdict(list)
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if self.compare(bank[i], bank[j]) == 1:
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])
        startlst = deque()
        visited = {}
        for b in bank:
            if self.compare(startGene, b) == 1:
                if b == endGene:
                    return 1
                startlst.append((b, 1))
                visited[b] = True

        while len(startlst) > 0:
            q = startlst.popleft()
            for adj in graph[q[0]]:
                if adj == endGene:
                    return q[1] + 1
                if adj not in visited:
                    startlst.append((adj, q[1] + 1))
                    visited[adj] = True
        return -1

    def compare(self, gen1, gen2):
        cnt = 0
        for g1, g2 in zip(gen1, gen2):
            if g1 != g2:
                cnt += 1
        return cnt
    
if __name__ == '__main__':
    s = Solution()
    print(s.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))