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
def solve(N, CP, Q, LR):
    class1 = [0]
    class2 = [0]
    for c, p in CP:
        class1.append(class1[-1] + (p if c == 1 else 0))
        class2.append(class2[-1] + (p if c == 2 else 0))

    for l, r in LR:
        print(class1[r] - class1[l - 1], class2[r] - class2[l - 1])


if __name__ == '__main__':
    N = int(input())
    CP = [[int(i) for i in input().split()] for _ in range(N)]
    Q = int(input())
    LR = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, CP, Q, LR)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
