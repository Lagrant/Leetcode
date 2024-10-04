from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        w_sizes = [len(w) + 1 for w in words]
        segs = []
        ws = []
        cnt = 0
        while cnt < len(words):
            seg = []
            w = 0
            while cnt < len(words) and w + w_sizes[cnt] - 1 <= maxWidth:
                w += w_sizes[cnt]
                seg.append(words[cnt])
                cnt += 1
            segs.append(seg)
            ws.append(w)

        for i in range(len(segs) - 1):
            res_w = maxWidth - ws[i] + 1
            if len(segs[i]) == 1:
                segs[i] += ' ' * res_w
                continue

            num_spaces = res_w // (len(segs[i]) - 1)
            extra_spaces = res_w % (len(segs[i]) - 1)
            for j in range(len(segs[i]) - 1):
                if j < extra_spaces:
                    segs[i][j] += ' ' * (num_spaces + 2)
                else:
                    segs[i][j] += ' ' * (num_spaces + 1)

        for i in range(len(segs[-1]) - 1):
            segs[-1][i] += ' '
        segs[-1][-1] += ' ' * (maxWidth - ws[-1] + 1)
        return [''.join(s) for s in segs]
    
if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))