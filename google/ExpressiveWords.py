class Solution:
    def expressiveWords(self, s: str, words) -> int:
        s_cnt = [[s[0], 0]]
        for c in s:
            if (c == s_cnt[-1][0]):
                s_cnt[-1][1] += 1
            else:
                s_cnt.append([c, 1])
        
        word_cnt = 0
        for word in words:
            if (len(word) > len(s)):
                continue
            ch = [[word[0], 0]]
            for w in word:
                if (w == ch[-1][0]):
                    ch[-1][1] += 1
                else:
                    ch.append([w, 1])
            flag = True
            if (len(s_cnt) != len(ch)):
                flag = False
                break
                
            for i in range(len(s_cnt)):
                if (s_cnt[i][0] == ch[i][0] and (s_cnt[i][1] == ch[i][1] or s_cnt[i][1] >= max(3, ch[i][1]))):
                    continue
                else:
                    flag = False
                    break
            if (flag):
                word_cnt += 1
        
        return word_cnt

sol = Solution()
print(sol.expressiveWords("aaa", ["aaaa"]))