class Solution:
    def decreaseDict(self, double_dict, num):
        if num in double_dict and double_dict[num] >= 2:
            double_dict[num] -= 1
        elif num in double_dict:
            double_dict.pop(num)

    def findOriginalArray(self, changed):
        if len(changed) % 2 == 1:
            return []

        changed.sort()
        double_dict = {}
        for num in changed:
            double_dict[num] = double_dict.get(num, 0) + 1
        res = []
        for num in changed:
            if num not in double_dict:
                continue
            if 2 * num in double_dict:
                self.decreaseDict(double_dict, 2 * num)
                res.append(num)
                self.decreaseDict(double_dict, num)
            elif num % 2 == 1:
                return []

        if any(double_dict):
            return []
        return res

sol = Solution()
print(sol.findOriginalArray([0]))