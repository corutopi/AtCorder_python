# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    import math
    A.sort()
    u = A[math.ceil(N / 2):]
    d = A[:math.ceil(N / 2)]

    ans1 = 0
    if N % 2 == 1:
        ans1 = 2 * sum(u) - (sum(d) + sum(d[:-2]))
    else:
        ans1 = sum(u) + sum(u[1:]) - (sum(d) + sum(d[:-1]))

    u = A[N // 2:]
    d = A[:N // 2]
    ans2 = 0
    if N % 2 == 1:
        ans2 = sum(u) + sum(u[2:]) - (sum(d) * 2)
    else:
        ans2 = sum(u) + sum(u[1:]) - (sum(d) + sum(d[:-1]))

    print(max(ans1, ans2))


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for i in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
