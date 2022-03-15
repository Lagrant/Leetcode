class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set()
        for jewel in jewels:
            jewel_set.add(jewel)
        
        cnt = 0
        for stone in stones:
            if (stone in jewel_set):
                cnt += 1
        
        return cnt