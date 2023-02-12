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
def solve(N, CSF):
    c, s, f = 0, 1, 2
    for i in range(N - 1):
        x = CSF[i][s] + CSF[i][c]
        for j in range(i + 1, N - 1):
            if CSF[j][s] >= x:
                x += CSF[j][s] - x
            else:
                x += CSF[j][f] - (x % CSF[j][f]) if x % CSF[j][f] != 0 else 0
            x += CSF[j][c]
        print(x)
    print(0)


if __name__ == '__main__':
    N = int(input())
    CSF = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, CSF)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
