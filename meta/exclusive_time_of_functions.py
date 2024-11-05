from typing import List
from collections import defaultdict
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exe_dict = defaultdict(int)
        for i, log in enumerate(logs):
            id, exe, t = self.parser(log)
            if i == 0:
                exe_dict[id] = t
                continue
            if exe == 'start':
                

    def parser(self, log):
        id, exe, t = log.split(':')
        id = int(id)
        t = int(t)
        return id, exe, t