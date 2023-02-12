# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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
def solve(N, Ma, Mb, ABC):
    x = N * 10 + 1
    dp = [[inf] * x for _ in range(x)]
    dp[0][0] = 0
    for a, b, c in ABC:
        # ケツから計算しないと同じ商品を複数回購入してしまう
        for i, j in ((i, j)
                     for i in range(x - a - 1, -1, -1)
                     for j in range(x - b - 1, -1, -1)):
            dp[i + a][j + b] = min(dp[i + a][j + b], dp[i][j] + c)
    ans = inf
    for m in range(1, x // Ma + 1):
        if x <= max(Ma * m, Mb * m): break
        ans = min(ans, dp[Ma * m][Mb * m])
    print(ans if ans != inf else -1)


if __name__ == '__main__':
    N, Ma, Mb = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, Ma, Mb, ABC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
