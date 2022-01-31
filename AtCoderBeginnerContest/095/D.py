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
def solve(N, C, xv):
    ans = 0
    revers_xv = [[0, 0]] + [[C - x, v] for x, v in reversed(xv)]
    xv = [[0, 0]] + xv

    right = [0]
    right_max = [0]
    right_turn = [0]
    right_turn_max = [0]
    for i in range(1, N + 1):
        x, v = xv[i]
        xd, vd = xv[i - 1]
        right.append(right[-1] - (x - xd) + v)
        right_max.append(max(right_max[-1], right[-1]))
        right_turn.append(right[-1] - x)
        right_turn_max.append(max(right_turn_max[-1], right_turn[-1]))

    left = [0]
    left_max = [0]
    left_turn = [0]
    left_turn_max = [0]
    for i in range(1, N + 1):
        x, v = revers_xv[i]
        xd, vd = revers_xv[i - 1]
        left.append(left[-1] - (x - xd) + v)
        left_max.append(max(left_max[-1], left[-1]))
        left_turn.append(left[-1] - x)
        left_turn_max.append(max(left_turn_max[-1], left_turn[-1]))

    for i in range(N + 1):
        ans = max(ans, right_max[i] + left_turn_max[N - i])
        ans = max(ans, left_max[i] + right_turn_max[N - i])

    print(ans)


if __name__ == '__main__':
    N, C = map(int, input().split())
    xv = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, C, xv)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, C = 10 ** 5, 10 ** 14
    # xv = [[x, randint(1, 10 ** 9)] for x in
    #       random_ints(N, 1, C, sort=True)]
    # solve(N, C, xv)
