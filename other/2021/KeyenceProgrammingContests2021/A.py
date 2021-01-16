# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, a, b):
    a_max = [a[0]]
    for i in range(1, N):
        a_max.append(max(a_max[-1], a[i]))
    ans = [a[0] * b[0]]
    for i in range(1, N):
        # 前回の値, 新しいBの値 * Aのとりうる最大値 の内大きいほう.
        ans.append(max(ans[-1], b[i] * a_max[i]))

    [print(i) for i in ans]


if __name__ == '__main__':
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    solve(N, a, b)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
