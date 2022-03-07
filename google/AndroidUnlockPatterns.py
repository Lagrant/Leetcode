from collections import defaultdict
class Solution:

    def numberOfPatterns(self, m: int, n: int) -> int:
        def search_pattern(cand, pat_len, pat_cnt, visited):
            pat_len += 1
            visited[cand] = True
            if (pat_len >= m and pat_len < n):
                pat_cnt += 1
            elif (pat_len == n):
                pat_cnt += 1
                visited[cand] = False
                return pat_cnt
            
            connect_len = len(connect[cand])
            block_lst = block[cand]
            for b in block_lst:
                if (visited[b]):
                    connect[cand].append(block_lst[b])
            for nxt in connect[cand]:
                if (visited[nxt]):
                    continue
                pat_cnt = search_pattern(nxt, pat_len, pat_cnt, visited)
            
            visited[cand] = False
            connect[cand] = connect[cand][:connect_len]
            return pat_cnt


        if (m > n):
            return
        
        connect = {
            1: [2, 4, 5, 6, 8],
            2: [1, 3, 4, 5, 6, 7, 9],
            3: [i for i in range(1, 10) if (i != 3 and i != 1 and i !=7 and i != 9)],
            4: [i for i in range(1,10) if (i != 4 and i != 6)],
            5: [i for i in range(1,10) if (i !=5)],
            6: [i for i in range(1,10) if (i != 6 and i != 4)],
            7: [2, 4, 5, 6, 8],
            8: [i for i in range(1,10) if (i != 8 and i != 2)],
            9: [2, 4, 5, 6, 8]
        }

        block = {
            1: {2: 3, 4: 7, 5: 9},
            2: {5: 8},
            3: {2: 1, 6: 9, 5: 7},
            4: {5: 6},
            5: {},
            6: {5: 4},
            7: {4: 1, 8: 9, 5: 3},
            8: {5: 2},
            9: {8: 7, 6: 3, 5: 1}
        }

        candidates = [1, 2, 5]
        pat_len = 0
        pat_cnt = 0
        for cand in candidates:
            visited = defaultdict(bool)
            cand_pat_cnt = search_pattern(cand, pat_len, 0, visited)
            if (cand != 5):
                pat_cnt += 4 * cand_pat_cnt
            else:
                pat_cnt += cand_pat_cnt
            

        return pat_cnt

        

sol = Solution()
print(sol.numberOfPatterns(3,3))