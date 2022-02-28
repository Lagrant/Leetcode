class Solution:
    def findReplaceString(self, s: str, indices, sources, targets) -> str:
        matched_lst = {}
        for i in range(len(indices)):
            idx = indices[i]
            tgt = targets[i]
            src = sources[i]
            if (s[idx:idx + len(src)] == src):
                matched_lst[idx] = [idx, idx + len(src), tgt]
        # matched_lst.sort(reverse=True, key=lambda x: x[0])
        rep_s = s
        for i in range(len(s)-1, -1, -1):
            if (i in matched_lst):
                rep_s = rep_s[:matched_lst[i][0]] + matched_lst[i][2] + rep_s[matched_lst[i][1]:]
        
        return rep_s