class Solution:
    def minChanges(self, s: str) -> int:
        cnt_s = []
        last_c = s[0]
        cnt = 0
        for c in s:
            if c == last_c:
                cnt += 1
            else:
                cnt_s.append(cnt)
                cnt = 1
                last_c = c
        cnt_s.append(cnt)
        idx, changes = 0, 0
        while idx < len(cnt_s) - 1:
            if cnt_s[idx] % 2 == 1:
                if cnt_s[idx + 1] % 2 == 1:
                    idx += 2
                else:
                    
                    cnt_s[idx + 1] += 1
                    idx += 1
                changes += 1
            else:
                idx += 1
        return changes
    def minChanges2(self, s: str) -> int:
   
        count = 0 
        for i in range(0,len(s) - 1, 2):
            if s[i ] != s[i +1]:
                count += 1
        return count


if __name__ == '__main__':
    slt = Solution()
    print(slt.minChanges('1001'))