from typing import List
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if len(words) == 0:
            return s
        positions = []
        for word in words:
            start = s.find(word)
            while start != -1:
                positions.append([start, start + len(word)])
                start = s.find(word, start + 1)
        if len(positions) == 0:
            return s
        
        positions.sort(key=lambda x: x[0])
        merged_positions = []
        cur_interv = positions[0]
        j = 1
        while j < len(positions):
            if cur_interv[0] <= positions[j][0] <= cur_interv[1]:
                if positions[j][1] > cur_interv[1]:
                    cur_interv[1] = positions[j][1]
            else:
                merged_positions.append(cur_interv)
                cur_interv = positions[j]
            j += 1
        merged_positions.append(cur_interv)
        tagged_str = [f'{s[0:merged_positions[0][0]]}']
        for i, pos in enumerate(merged_positions):
            subs = s[pos[0] : pos[1]]
            if i != len(merged_positions) - 1:
                subs2 = s[pos[1] : merged_positions[i + 1][0]]
            else:
                subs2 = s[pos[1]:]
            tagged_str.append(f'<b>{subs}</b>{subs2}')
        return ''.join(tagged_str)

if __name__ == '__main__':
    s = Solution()
    print(s.addBoldTag("abcxyz123", ["abc","123"]))