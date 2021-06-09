# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S):
    STRING = 'atcoder'
    dp = [1] + [0] * len(STRING)
    str_map = {}
    for i, s in enumerate(STRING):
        str_map.setdefault(s, [])
        str_map[s].append(i + 1)
    for s in S:
        dp_new = dp.copy()
        if s not in str_map.keys(): continue
        for i in str_map[s]:
            dp_new[i] = (dp[i - 1] + dp[i]) % mod
        dp = dp_new
    print(dp[-1])


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
