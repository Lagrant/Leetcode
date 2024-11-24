from typing import List
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1, s2):
            i, j = 0, 0
            while i != len(s1) - 1 or j != len(s2) - 1:
                if s1[i] == s2[j]:
                    i = (i + 1) % len(s1)
                    j = (j + 1) % len(s2)
                else:
                    return ord(s1[i]) - ord(s2[j])
            return ord(s1[i]) - ord(s2[j])

                    
        snums = [str(n) for _, n in enumerate(nums)]
        snums = sorted(snums, key=functools.cmp_to_key(compare), reverse=True)
        snums = ''.join(snums)
        return str(int(snums))

if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10,2]))