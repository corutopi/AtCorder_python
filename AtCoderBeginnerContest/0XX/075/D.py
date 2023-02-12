# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, xy):
    x = sorted([x for x, y in xy])
    y = sorted([y for x, y in xy])
    cumsum_2d = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            xi = x[i]
            yi = y[j]
            for xx, yy in xy:
                if xx <= xi and yy <= yi:
                    cnt += 1
            cumsum_2d[i + 1][j + 1] = cnt

    ans = 10 ** 100
    for i in range(N):
        for j in range(i, N):
            for m in range(N):
                for n in range(m, N):
                    cnt = cumsum_2d[j + 1][n + 1] - \
                          cumsum_2d[j + 1][m] - \
                          cumsum_2d[i][n + 1] + \
                          cumsum_2d[i][m]
                    if cnt >= K:
                        ans = min(ans, abs(x[i] - x[j]) * abs(y[m] - y[n]))
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, xy)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # N, K = 50, randint(2, 50)
    # xy = [[randint(-10 ** 9, 10 ** 9), randint(-10 ** 9, 10 ** 9)] for _ in
    #       range(N)]
    # solve(N, K, xy)
