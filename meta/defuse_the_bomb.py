from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new_c = [0] * len(code)
        for i, c in enumerate(code):
            if k > 0:
                if k + i < len(code):
                    new_c[i] = sum(code[i + 1: i + k + 1])
                else:
                    sub = k + i - len(code)
                    new_c[i] = sum(code[i + 1:]) + sum(code[:sub + 1])
            elif k == 0:
                new_c[i] = 0
            else:
                if k + i >= 0:
                    new_c[i] = sum(code[k + i:i])
                else:
                    new_c[i] = sum(code[:i]) + sum(code[k + i:])
        return new_c
            