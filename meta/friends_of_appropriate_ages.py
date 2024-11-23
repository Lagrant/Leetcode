from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        reqs = 0
        i = len(ages) - 1
        while i >= 0:
            piv = ages[i] // 2 + 7
            if piv >= ages[i]:
                i -= 1
                continue
            tempk = 1
            while i - tempk >= 0 and ages[i] == ages[i - tempk]:
                tempk += 1
            rep = tempk * (tempk - 1)
            i = i - tempk + 1

            piv_idx = self.bin_search(ages[:i + 1], piv)
            reqs = reqs + (i - piv_idx) * tempk + rep
            i -= 1
        return reqs


    def numFriendRequests2(self, ages: List[int]) -> int:
        if not ages:
            return 0 

        requests = 0 
        
        count = [0 for _ in range(122)]
        prefix = [0 for _ in range(122)]


        for age in ages:
            count[age] += 1

        for age in range(15, 122):
            prefix[age] = prefix[age - 1] + count[age]

            min_age = int(0.5 * age + 7) + 1

            # total: num of people that is greater than or equal to min_age 
            # and smaller than or equal to age.
            total = prefix[age] - prefix[min_age - 1]


            requests += count[age] * (total - 1)
        
        return requests  

    def bin_search(self, arr, piv):
        i, j = 0, len(arr) - 1
        while abs(i - j) > 1:
            mid = (i + j) // 2
            if arr[mid] > piv:
                j = mid
            elif arr[mid] < piv:
                i = mid
            else:
                while arr[mid] == piv:
                    mid += 1
                return mid
        
        return j if arr[i] <= piv else i
    
if __name__ == '__main__':
    s = Solution()
    print(s.numFriendRequests([16,16]))