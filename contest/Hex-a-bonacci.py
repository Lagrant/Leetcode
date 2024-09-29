def dp(n, base):
    dp_list = base.copy()
    
    if n < len(base):
        return dp_list[n]
    else:
        for i in range(len(base), n+1):
            dp_list.append(dp_list[-1] + dp_list[-2] + dp_list[-3] + dp_list[-4] + dp_list[-5] + dp_list[-6])
        return dp_list[-1]

cases = int(input())
for case in range(cases):
    inputs = input().split(' ')
    a, b, c, d, e, f, n = map(lambda x: int(x), inputs)
    base = [a, b, c, d, e, f]
    print('Case {}: {}'.format(case+1, dp(n, base) % 10000007))
