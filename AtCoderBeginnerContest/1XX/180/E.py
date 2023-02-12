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
def solve(N, XYZ):
    costmap = [[0] * N for _ in range(N)]
    # 別の場所を経由したほうが早く着く場合が考慮できていない
    # → と思ったけど別に考慮する必要ない気がしてきたのでこのままだしてみる
    # → 無かった。
    for i, j in ((i, j) for i in range(N) for j in range(N)):
        costmap[i][j] = abs(XYZ[j][0] - XYZ[i][0]) + \
                        abs(XYZ[j][1] - XYZ[i][1]) + \
                        max(0, XYZ[j][2] - XYZ[i][2])

    # min route that visited bit(i)=1 town and last visited town is j
    dp = [[inf] * N for _ in range(2 ** N)]
    dp[1] = [inf] * N
    dp[1][0] = 0
    for i in range(3, 2 ** N, 2):
        for j in range(N):
            if i >> j & 1 == 0: continue
            new_cost = inf
            bf_route = i ^ (2 ** j)
            for k in range(N):
                new_cost = min(new_cost, dp[bf_route][k] + costmap[k][j])
            dp[i][j] = new_cost

    print(min([dp[-1][x] + costmap[x][0] for x in range(N)]))


if __name__ == '__main__':
    N = int(input())
    XYZ = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XYZ)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
