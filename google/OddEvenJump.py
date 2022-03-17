class Solution:
    def oddJump(self, cur, arr):
        small = 1e5+1
        pos = -1
        for i in range(len(arr)):
            if (arr[i] >= cur and arr[i] < small):
                small = arr[i]
                pos = i
        return pos
    
    def evenJump(self, cur, arr):
        larg = -1
        pos = -1
        for i in range(len(arr)):
            if (arr[i] <= cur and arr[i] > larg):
                larg = arr[i]
                pos = i
        return pos

    def buildSmall(self, cur, arr, larg_vals, cut_len):
        larg = [1e5+1, -1]
        for i, lv in zip(range(len(arr)), reversed(larg_vals)):
            if (cur > arr[i]):
                if (cur > lv[0]):
                    # return larg if (larg[0] < 1e5+1) else [-1, -1]
                    continue
                else:
                    cur_larg = lv.copy()
                    return cur_larg if (larg[0] > cur_larg[0]) else larg
            elif (cur == arr[i]):
                return [arr[i], i + cut_len]
            else:
                if (larg[0] > arr[i]):
                    larg[0]= arr[i]
                    larg[1] = i + cut_len
        return larg

    def buildlarg(self, cur, arr, small_vals, cut_len):
        small = [-1, -1]
        for i, sv in zip(range(len(arr)), reversed(small_vals)):
            if (cur < arr[i]):
                if (cur < sv[0]):
                    # return small
                    continue
                else:
                    cur_small = sv.copy()
                    return cur_small if (small[0] < cur_small[0]) else small
            elif (cur == arr[i]):
                return [arr[i], i + cut_len]
            else:
                if (small[0] < arr[i]):
                    small[0] = arr[i]
                    small[1] = i + cut_len
        return small

    def oddEvenJumps(self, arr) -> int:
        count = 1
        # larg_lst = [-2] * len(arr)
        # small_lst = [-2] * len(arr)
        larg_lst = [[arr[-1], len(arr) - 1]]
        small_lst = [[arr[-1], len(arr) - 1]]
        for i in reversed(range(len(arr) - 1)):
            larg_lst.append(self.buildlarg(arr[i], arr[i+1:], larg_lst, i+1))
            small_lst.append(self.buildSmall(arr[i], arr[i+1:], small_lst, i+1))
        larg_lst = list(reversed(larg_lst))
        small_lst = list(reversed(small_lst))

        for i in range(len(arr)-1):
            j = i
            jump = 1
            while (j < len(arr)):
                if (jump % 2 == 0):
                    if (larg_lst[j][1] == -1):
                        break
                    else:
                        j = larg_lst[j][1]
                        jump += 1
                else:
                    if (small_lst[j][1] == -1):
                        break
                    else:
                        j = small_lst[j][1]
                        jump += 1
                if (j == len(arr) - 1):
                    count += 1
                    break
        return count

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        cmb = sorted([(i, x) for i, x in enumerate(arr)], key=lambda x:x[1])  # sort by value and keep index order
        nxt = [[None, None] for _ in range(len(arr))]   # [[odd_nxt, even_nxt]]
        S = []
        for i, _ in cmb:
            while len(S)>0 and S[-1]<=i:
                nxt[S.pop()][0] = i
            S.append(i)
        cmb.sort(key=lambda x:x[1], reverse=True)   # sort by value and keep index order
        S = []
        for i, _ in cmb:
            while len(S)>0 and S[-1]<=i:
                nxt[S.pop()][1] = i
            S.append(i)
        
        @cache
        def DP(i, is_even):
            if i == len(arr)-1: return True
            if nxt[i][is_even] is None: return False
            return DP(nxt[i][is_even], ~is_even)
        
        count = 0
        for i in range(len(arr)):
            if DP(i, 0) is True: count += 1
        
        return count

sol = Solution()
print(sol.oddEvenJumps([10,13,12,14,15]))