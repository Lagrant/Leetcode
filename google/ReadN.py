# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
class Solution:
    def __init__(self) -> None:
        self.bufn = []
        self.bufn_idx = 0

    def read(self, buf, n: int) -> int:
        cur = 0
        buf4 = [''] * 4
        while (cur < n):
            if (len(self.bufn) == 0):
                size4 = read4(buf4)
                if (size4 == 0):
                    return cur
                self.bufn = buf4
                self.bufn_idx = 0
            else:
                buf4 = self.bufn
                size4 = len(self.bufn) - self.bufn_idx
            if (n > cur + size4):
                buf[cur:cur + size4] = buf4[self.bufn_idx:self.bufn_idx + size4]
                self.bufn = []
                self.bufn_idx = 0
                cur += size4
            else:
                buf[cur:n] = buf4[self.bufn_idx:self.bufn_idx + n - cur]
                self.bufn_idx = self.bufn_idx + n - cur
                cur = n
            buf4 = [''] * 4
        return cur