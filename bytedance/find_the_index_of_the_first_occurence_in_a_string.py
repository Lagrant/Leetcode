class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                continue
            i += 1
            cur_j = j
            while j >= 0 and i + len(needle) - 1 - j < len(haystack):
                if haystack[i] == needle[j]:
                    i -= 1
                    j -= 1
                    continue
                i += 1
                cur_j = j
            
            if j < 0:
                j = cur_j
                i += cur_j + 1
        if j == len(needle):
            return i - j
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr('mississippi', 'issipi'))