# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    ans = - 50 * 50
    for i in range(N):
        max_aoki = - 50 * 50
        p_takahashi = 0
        for j in range(N):
            if i == j: continue
            takahashi = 0
            aoki = 0
            l, r = min(i, j), max(i, j)
            for k in range(l, r + 1):
                if (k - l) % 2 == 0:
                    takahashi += A[k]
                else:
                    aoki += A[k]
            if aoki > max_aoki:
                max_aoki = aoki
                p_takahashi = takahashi
        ans = max(ans, p_takahashi)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 50
    # A = [randint(-50, 50) for _ in range(N)]
    # solve(N, A)
