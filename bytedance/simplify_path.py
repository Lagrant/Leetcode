import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return '/'
        idx = 1
        n_stack = ['/']
        while idx < len(path):
            s, idx = self.parse_next_folder(path, idx)
            if s == './':
                continue
            if s == '../':
                if len(n_stack) > 1:
                    n_stack.pop()
            else:
                n_stack.append(s)
        if len(n_stack) > 1 and n_stack[-1].endswith('/'):
            n_stack[-1] = n_stack[-1][:-1]
        return ''.join(n_stack)

    def parse_next_folder(self, path, start):
        while start < len(path) and path[start] == '/':
            start += 1
        s1 = ''
        while start < len(path) and path[start] != '/':
            s1 += path[start]
            start += 1
        s1 += '/'
        while start + 1 < len(path) and path[start + 1] == '/':
            start += 1
        return s1, start + 1
    
    def simplifyPath1(self, path: str) -> str:
        path = re.sub(r'/{2,}', '/', path)
        dirs = [segment for segment in path.split('/') if segment]
        stack = []

        for d in dirs:
            if d == ".":
                continue
            if d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return "/"+"/".join(stack)
    
if __name__ == '__main__':
    so = Solution()
    print(so.simplifyPath('///'))