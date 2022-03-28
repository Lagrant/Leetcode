class Solution:
    def __init__(self) -> None:
        self.max_int = 2**31 - 1
        self.min_int = -2**31
    def reverse(self, x: int) -> int:
        if (x == 0):
            return 0
        
        str_x = str(x)
        reverse_x = ''
        if (str_x[0] == '-'):
            reverse_x += '-'
            str_x = str_x[1:]
        
        for i in range(len(str_x) - 1, -1, -1):
            reverse_x += str_x[i]
        
        reverse_x = int(reverse_x)
        if (reverse_x > self.max_int or reverse_x < self.min_int):
            return 0
        return reverse_x