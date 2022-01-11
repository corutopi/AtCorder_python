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
def solve(N, xy):
    ans = 0
    for i, j in ((i, j) for i in range(N) for j in range(N)):
        ans = max(ans, (abs(xy[i][0] - xy[j][0]) ** 2 + abs(xy[i][1] - xy[j][1]) ** 2) ** 0.5)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, xy)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
