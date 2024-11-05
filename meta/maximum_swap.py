class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = list(str(num))
        snum = list(map(lambda x: int(x), snum))
        n_dict = {}
        for i, n in enumerate(snum):
            n_dict[n] = i
        ordernum = sorted(snum, key=lambda x: -x)

        j = 0
        for i, n in enumerate(snum):
            if n == ordernum[i]:
                continue
            j = n_dict[ordernum[i]]
            snum[i], snum[j] = snum[j], snum[i]
            break
        
        snum = ''.join(map(lambda x: str(x), snum))
        return int(snum)