class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) == 1 and len(abbr) == 1:
            return word == abbr or abbr == '1'
        
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                j += 1
                i += 1
                continue
            if not ('0' < abbr[j] <= '9'):
                return False
            subs, subidx = self.parse_integer(abbr[j:])
            subint = int(subs)
            j += subidx
            i += subint
            if i > len(word):
                return False
        return j == len(abbr) and i == len(word)
            
    def parse_integer(self, sint):
        idx = 0
        cum = ''
        while idx < len(sint) and '0' <= sint[idx] <= '9':
            cum += sint[idx]
            idx += 1
        return cum, idx

if __name__ == '__main__':
    s = Solution()
    print(s.validWordAbbreviation("internationalization", "i12iz4n"))