from typing import List
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        num = []
        while i < len(encoded1) and j < len(encoded2):
            if encoded1[i][1] < encoded2[j][1]:
                temp = encoded1[i][0] * encoded2[j][0]
                encoded2[j][1] -= encoded1[i][1]
                if len(num) > 0 and num[-1][0] == temp:
                    num[-1][1] += encoded1[i][1]
                else:
                    num.append([temp, encoded1[i][1]])
                i += 1
            elif encoded1[i][1] >= encoded2[j][1]:
                temp = encoded1[i][0] * encoded2[j][0]
                if len(num) > 0 and num[-1][0] == temp:
                    num[-1][1] += encoded2[j][1]
                else:
                    num.append([temp, encoded2[j][1]])
                encoded1[i][1] -= encoded2[j][1]
                if encoded1[i][1] == 0:
                    i += 1
                j += 1
        return num