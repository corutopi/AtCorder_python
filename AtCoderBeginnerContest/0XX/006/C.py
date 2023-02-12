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
def solve(N, M):
    if M < N * 2 or N * 4 < M:
        print(-1, -1, -1)
        return
    leg = N * 2
    # a = N  # adult
    # o = 0  # old
    # b = 0  # baby
    # while leg < M:
    #     if M - leg >= 2:
    #         a -= 1
    #         b += 1
    #         leg += 2
    #     else:
    #         a -= 1
    #         o += 1
    #         leg += 1

    # more smart
    a = N  # adult
    b, o = divmod(M - leg, 2)
    a -= b + o
    print(a, o, b)


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
