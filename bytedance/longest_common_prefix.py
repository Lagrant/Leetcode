from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []
        for j in range(len(strs[0])):
            common.append(strs[0][j])
            breakflag = False
            for i in range(1, len(strs)):
                if len(strs[i]) <= j or strs[i][j] != common[-1]:
                    breakflag = True
                    break
            if breakflag:
                return ''.join(common[:-1])
        return ''.join(common)

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['ab', 'a']))