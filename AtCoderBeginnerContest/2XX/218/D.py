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
    xy.sort(key=lambda x: x[0])
    dict_xy = {str(xyi[0]) + '_' + str(xyi[1]): 1 for xyi in xy}
    ans = 0
    for i, j in ((i, j) for i in range(N) for j in range(i + 1, N)):
        if xy[i][0] == xy[j][0] or xy[i][1] == xy[j][1]:
            continue
        a = str(xy[i][0]) + '_' + str(xy[j][1])
        b = str(xy[j][0]) + '_' + str(xy[i][1])
        if dict_xy.get(a, 0) + dict_xy.get(b, 0) == 2:
            ans += 1
    print(ans // 2)


if __name__ == '__main__':
    N = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, xy)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2000
    # xy = [[randint(0, 10), randint(0, 10)] for _ in range(N)]
    # solve(N, xy)
