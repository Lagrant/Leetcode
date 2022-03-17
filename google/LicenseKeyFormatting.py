class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cnt = 0
        new_s = ''
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == '-'):
                # s = s[:i] + s[i+1:]
                continue
            cnt += 1
            if (cnt == k + 1):
                # s[i].upper()
                # s = s[:i] + s[i].upper() + '-' + s[i+1:]
                new_s = s[i].upper() + '-' + new_s
                cnt = 1
            else:
                # s = s[:i] + s[i].upper() + s[i+1:]
                new_s = s[i].upper() + s[i+1:]
        
        return new_s

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-",'')
        s = s.upper()[::-1]
        return "-".join(s[i:i+k] for i in range(0, len(s), k))[::-1]
        
sol = Solution()
print(sol.licenseKeyFormatting("2-5g-3-J", 2))