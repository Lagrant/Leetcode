from collections import OrderedDict
class Solution:
    def totalFruit(self, fruits) -> int:
        basket = OrderedDict()
        amount = 0
        max_amt = -float('inf')
        for fruit in fruits:
            if (len(basket.keys()) < 2):
                basket[fruit] = basket.get(fruit, 0) + 1
                amount += 1
            elif (fruit in basket):
                flag = False
                amount += 1
                for f_type in basket:
                    if (f_type == fruit):
                        flag = True
                        break
                    break
                if (flag):
                    basket.popitem(last=False)
                    basket[fruit] = 1
                else:
                    basket[fruit] += 1
            else:
                max_amt = amount if (amount > max_amt) else max_amt
                basket.popitem(last=False)
                for f in basket:
                    amount = basket[f] + 1
                basket[fruit] = 1
        
        return amount if (amount > max_amt) else max_amt

sol = Solution()
print(sol.totalFruit([1,2,3,2,2]))