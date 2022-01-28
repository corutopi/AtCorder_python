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
def solve(N, M, st):
    room_clean = [0] * (N + 1)
    room_start = [0] * (N + 1)
    room_end = [0] * (N + 1)
    for s, t in st:
        room_start[s] += 1
        room_end[t] += 1

    cleaner = 0
    for i in range(N + 1):
        cleaner += room_start[i]
        room_clean[i] = 0 if cleaner <= 1 else 1
        cleaner -= room_end[i]

    room_cumsum = [0]
    for i in range(1, N + 1):
        room_cumsum.append(room_cumsum[-1] + room_clean[i])

    squeeze = []
    for i in range(M):
        s, t = st[i]
        if room_cumsum[t] - room_cumsum[s - 1] == t - s + 1:
            squeeze.append(i + 1)

    print(len(squeeze))
    [print(s) for s in squeeze]


if __name__ == '__main__':
    N, M = map(int, input().split())
    st = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, st)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 3 * 10 ** 5
    # M = 10 ** 5
    # st = [random_ints(2, 1, N, True, True) for _ in range(M)]
    # solve(N, M, st)
