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
def solve(S):
    base_str = 'chokudai'  # 同じ文字があるとダメ
    chokudai_map = {s: i + 1 for i, s in enumerate(base_str)}
    dp = [1] + [0] * len(base_str)
    for s in S:
        if chokudai_map.get(s, 'X') != 'X':
            dp[chokudai_map[s]] += dp[chokudai_map[s] - 1]
            dp[chokudai_map[s]] %= mod
    print(dp[-1])


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
