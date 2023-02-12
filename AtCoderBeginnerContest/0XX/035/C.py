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
def solve(N, Q, lr):
    left = [0] * N
    right = [0] * (N + 1)
    for l, r in lr:
        left[l - 1] += 1
        right[r] += 1
    revers = 0
    ans = []
    for i in range(N):
        revers += left[i]
        revers -= right[i]
        ans.append(revers % 2)
    print(''.join([str(i) for i in ans]))


if __name__ == '__main__':
    N, Q = map(int, input().split())
    lr = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, lr)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
