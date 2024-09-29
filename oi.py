# import math
# cases = int(input())

# for case in range(cases):
#     campnum, nights = map(int, input().split(' '))
#     days = nights + 1
#     milages = [0]
#     camps = []
#     for i in range(campnum):
#         camps.append(int(input()))
#     mean_dis = math.ceil(sum(camps) / campnum)
#     upper = mean_dis
#     cnt = 0
#     for i in range(days):
#         while milages[-1] < upper:
#             milages[-1] += camps[cnt]
#             cnt += 1

import os, io, sys

# def get_ints():
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#     s = input().decode()
#     list(map(int, s.split()))
#     return s

import sys
cases = int(input())
for case in range(cases):
    print(f'Case {case+1}:')
    n, q = list(map(int, sys.stdin.readline().strip().split()))
    sacks = list(map(int, sys.stdin.readline().strip().split()))
    outputs = []
    for i in range(q):
        op = list(map(int, sys.stdin.readline().strip().split()))
        if op[0] == 1:
            outputs.append(sacks[op[1]])
            sacks[op[1]] = 0
        elif op[0] == 2:
            sacks[op[1]] += op[2]
        else:
            outputs.append(sum(sacks[op[1]:op[2]+1]))
    output_str = '\n'.join(map(str, outputs))
    print(output_str)
