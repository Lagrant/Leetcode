from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end = len(numbers) - 1
        start = 0
        while start < end:
            if numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                return [start + 1, end + 1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([-1, 0], -1))