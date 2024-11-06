from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = [] # (int_func, int_start)

        out = [0]*n
        lasttimestamp = 0
        for log in logs:
            vals = log.split(':')
            if vals[1] == 'start':
                if len(stk) > 0:
                    if lasttimestamp != stk[-1][1]:
                        out[stk[-1][0]] += int(vals[2]) - lasttimestamp - 1
                    else:
                        out[stk[-1][0]] += int(vals[2]) - lasttimestamp
                stk.append((int(vals[0]), int(vals[2])))
            
            if vals[1] == 'end':
                t = stk.pop()
                if lasttimestamp == t[1]:
                    out[t[0]] += int(vals[2]) - lasttimestamp + 1
                else:
                    out[t[0]] += int(vals[2]) - lasttimestamp

            lasttimestamp = int(vals[2])
        
        return out

        