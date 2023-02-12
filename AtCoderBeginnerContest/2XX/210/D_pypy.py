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
def solve(H, W, C, A):
    ans = inf
    for i in range(4):
        if i % 2 == 0:
            A = A[::-1]
        else:
            A = [a[::-1] for a in A]

        dp = [[0] * W for _ in range(H)]
        for h, w in ((h, w) for h in range(H) for w in range(W)):
            if h == w == 0:
                dp[h][w] = A[h][w] * 2
                continue
            if h == 0:
                dp[h][w] = min(dp[h][w - 1] - A[h][w - 1] + C + A[h][w],
                               A[h][w - 1] + C + A[h][w])
                continue
            if w == 0:
                dp[h][w] = min(dp[h - 1][w] - A[h - 1][w] + C + A[h][w],
                               A[h - 1][w] + C + A[h][w])
                continue
            dp[h][w] = min(dp[h][w - 1] - A[h][w - 1] + C + A[h][w],
                           dp[h - 1][w] - A[h - 1][w] + C + A[h][w],
                           A[h][w - 1] + C + A[h][w],
                           A[h - 1][w] + C + A[h][w])
        dp[0][0] = inf
        ans = min(ans, min(min(d) for d in dp))
    return ans


def solve_force(H, W, C, A):
    ans = inf
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        for h2, w2 in ((h2, w2) for h2 in range(H) for w2 in range(W)):
            if h == h2 and w == w2:
                continue
            ans = min(ans,
                      A[h][w] + A[h2][w2] + C * (abs(h - h2) + abs(w - w2)))
    return ans


if __name__ == '__main__':
    H, W, C = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    print(solve(H, W, C, A))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # i = 0
    # while True:
    #     i += 1
    #     H, W, C = 3, 4, randint(1, 10)
    #     A = [[randint(1, 10) for _ in range(W)] for _ in range(H)]
    #     x, y = solve(H, W, C, A) , solve_force(H, W, C, A)
    #     if x != y:
    #         print(H, W, C)
    #         [print(' '.join(str(i) for i in a)) for a in A]
    #         print('xxxxx')
    #         print(x, y)
    #         break
    #     if i % 100 == 0:
    #         print(i)
