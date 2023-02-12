# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, A, XY):
    dp = [inf] * (N + 1)
    town_map = [[] for _ in range(N + 1)]
    for x, y in XY:
        town_map[x].append(y)
    for i in range(1, N + 1):
        for t in town_map[i]:
            dp[t] = min(dp[t], min(dp[i], A[i - 1]))
    ans = - inf
    for i in range(1, N + 1):
        ans = max(ans, A[i - 1] - dp[i])
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    XY = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, A, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
