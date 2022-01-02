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
def solve(N, M, abc):
    short_map = [[inf] * N for _ in range(N)]
    for a, b, c in abc:
        short_map[a - 1][b - 1] = min(short_map[a - 1][b - 1], c)
        short_map[b - 1][a - 1] = min(short_map[b - 1][a - 1], c)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                short_map[j][k] = min(short_map[j][k],
                                      short_map[j][i] + short_map[i][k])
    ans = 0
    for a, b, c in abc:
        ans += 1 if short_map[a - 1][b - 1] < c else 0
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    abc = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, abc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
