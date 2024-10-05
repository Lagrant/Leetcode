from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        max_e = rows * cols
        arr = []
        layer = 0
        while len(arr) < max_e:
            arr.extend(self.move_rd(matrix[layer][layer: cols - layer]))
            arr.extend(self.move_rd([matrix[i][-layer - 1] for i in range(layer + 1, rows - layer)]))
            arr.extend(self.move_lu(matrix[-layer - 1][layer:-layer-1]))  
            arr.extend(self.move_lu([matrix[i][layer] for i in range(layer + 1, rows - layer - 1)]))
            layer += 1

        return arr[:max_e]
    
    def move_rd(self, arr):
        return arr
    def move_lu(self, arr):
        return arr[::-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))