class Neg:
    def __init__(self, idx=None, start=-1, end=-1) -> None:
        self.idx = idx
        self.start = start
        self.end = end
class Solution1:
    """
    since negative value can flip the array, we need to
    maintain two variables: max_so_far and min_so_far
    """
    def maxProduct(self, nums) -> int:
        dp_table = [nums[0]]
        max_prod = []
        negs = [Neg([], 0)]
        if (nums[0] < 0):
            negs[-1].idx.append(0)
        for i in range(1, len(nums)):
            if (dp_table[-1] == 0):  
                dp_table.append(nums[i])
                negs[-1].end = i - 2
                negs.append(Neg([], i - 1, i - 1))
                negs.append(Neg([], i))
                if (nums[i] < 0):
                    negs[-1].idx.append(i)
                continue
            dp_table.append(nums[i] * dp_table[-1])
            if (nums[i] < 0):
                negs[-1].idx.append(i)
        if (negs[-1].end == -1):
            # negs[-1].end = len(nums) - 1
            for i in range(len(nums) - 1, -1, -1):
                if (nums[i] != 0):
                    negs[-1].end = i
                    break
        for neg in negs:
            if (len(neg.idx) % 2 == 0):
                max_prod.append(dp_table[neg.end])
            else:
                if (neg.end == neg.start):
                    max_prod.append(dp_table[neg.start])
                else:
                    m1 = dp_table[neg.idx[-1] - 1] if (neg.idx[-1] > 0) else dp_table[neg.idx[-1]]
                    m2 = int(dp_table[neg.end] / dp_table[neg.idx[0]])
                    max_prod.append(m2)
                    max_prod.append(max(m1, m2))

        _max_val = max(max_prod)
        if (_max_val < 0 and 0 in nums):
            return 0
        return _max_val


class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result

sol = Solution()
print(sol.maxProduct([-1, -1, 0]))
