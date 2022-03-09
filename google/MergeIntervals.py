from collections import deque
class Solution:
    """
    Consider the corner case that one start is the exactly other end
    """
    def merge(self, intervals):
        serials = []
        for interv in intervals:
            serials.append([interv[0], True])
            serials.append([interv[1], False])
        serials.sort(key=lambda x: x[0])


        serialized = []
        stack_seri = deque([])
        for seri in serials:
            if (seri[1]):
                if (len(stack_seri) == 0):
                    if (len(serialized) > 0 and serialized[-1][-1] == seri[0]):
                        serialized[-1].pop()
                    else:
                        serialized.append([seri[0]])
                    stack_seri.append(seri[0])
                else:
                    stack_seri.append(seri[0])
            else:
                stack_seri.pop()
                if (len(stack_seri) == 0):
                    serialized[-1].append(seri[0])
        
        return serialized

sol = Solution()
print(sol.merge([[1,4],[4,5],[4,9],[15,18]]))