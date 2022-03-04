from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        de_que = deque([])
        for c in s:
            if (c != ']'):
                de_que.append(c)
                continue
            
            cc = de_que.pop()
            sub_str = ''
            while (len(de_que) > 0 and cc != '['):
                sub_str = cc + sub_str
                cc = de_que.pop()
            
            if (len(de_que) == 0):
                return sub_str
            
            sub_num = ''
            while (len(de_que) > 0 and de_que[-1] >= '0' and de_que[-1] <= '9'):
                cc = de_que.pop()
                sub_num = cc + sub_num
                # cc = de_que.pop()
            
            if (sub_num != ''):
                sub_num = int(sub_num)
                sub_str = sub_str * sub_num
                de_que.append(sub_str)
            else:
                de_que.append(sub_str)
                return ''.join(de_que)

        if (len(de_que) > 0):
            return ''.join(de_que)
        
        return ''
