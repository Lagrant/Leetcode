from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i, piv = 0, 0
        cnt = 0
        while i < len(chars) - 1:
            cnt += 1
            if chars[i] != chars[i + 1]:
                if cnt == 1:
                    chars[piv] = chars[i]
                    piv += 1
                else:
                    s_cnt = list(str(cnt))
                    chars[piv] = chars[i]
                    chars[piv + 1: piv + 1 + len(s_cnt)] = s_cnt
                    
                    piv += 1 + len(s_cnt)
                
                cnt = 0
            i += 1
        cnt += 1
        if cnt == 1:
            chars[piv] = chars[-1]
            piv += 1
        else:
            s_cnt = list(str(cnt))
            chars[piv] = chars[-1]
            chars[piv + 1: piv + 1 + len(s_cnt)] = s_cnt
            piv += 1 + len(s_cnt)
        return piv
    
if __name__ == '__main__':
    s = Solution()
    print(s.compress(["a","a","a","a","b","a"]))