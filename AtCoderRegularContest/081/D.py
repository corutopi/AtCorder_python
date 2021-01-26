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
def solve(N, S1, S2):
    v, h = 1, 0  # vertical, horizon
    domino = []
    i = 0
    while i < N:
        if S1[i] == S2[i]:
            domino.append(v)
            i += 1
        else:
            domino.append(h)
            i += 2

    dp = 3 if domino[0] == v else 6
    for i in range(1, len(domino)):
        if domino[i - 1] == v and domino[i] == v:
            dp *= 2
        elif domino[i - 1] == v and domino[i] == h:
            dp *= 2
        elif domino[i - 1] == h and domino[i] == v:
            pass
        elif domino[i - 1] == h and domino[i] == h:
            dp *= 3
        dp %= mod

    print(dp)


if __name__ == '__main__':
    N = int(input())
    S1, S2 = input(), input()
    solve(N, S1, S2)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
