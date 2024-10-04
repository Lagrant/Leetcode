class Solution:
    def romanToInt(self, s: str) -> int:
        char_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        cnt = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and char_map[s[i]] < char_map[s[i + 1]]:
                cnt += char_map[s[i + 1]] - char_map[s[i]]
                i += 2
                continue
            cnt += char_map[s[i]]
            i += 1
        return cnt