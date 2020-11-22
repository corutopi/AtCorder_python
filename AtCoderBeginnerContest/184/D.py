# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B, C):
    dp = [[[[0, 0, False] for _ in range(101)] for _ in range(101)] for _ in
          range(101)
          ]
    dp[A][B][C] = [0, 1, True]
    dq = deque([[A, B, C]])
    while dq:
        a, b, c = dq.popleft()
        num, pattern, ald = dp[a][b][c]
        if a > 0:
            dp[a + 1][b][c][0] = num + 1
            dp[a + 1][b][c][1] += pattern * (a / (a + b + c))
            if a + 1 < 100 and dp[a + 1][b][c][2] is False:
                dq.append([a + 1, b, c])
                dp[a + 1][b][c][2] = True
        if b > 0:
            dp[a][b + 1][c][0] = num + 1
            dp[a][b + 1][c][1] += pattern * (b / (a + b + c))
            if b + 1 < 100 and dp[a][b + 1][c][2] is False:
                dq.append([a, b + 1, c])
                dp[a][b + 1][c][2] = True
        if c > 0:
            dp[a][b][c + 1][0] = num + 1
            dp[a][b][c + 1][1] += pattern * (c / (a + b + c))
            if c + 1 < 100 and dp[a][b][c + 1][2] is False:
                dq.append([a, b, c + 1])
                dp[a][b][c + 1][2] = True
    prb_map = [0] * 300
    for h in range(101):
        for i in range(101):
            for j in range(101):
                if 100 in [h, i, j]:
                    n, p, x = dp[h][i][j]
                    prb_map[n] += p
    ans = 0
    for s in range(len(prb_map)):
        ans += s * prb_map[s]
    print(ans)


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    solve(A, B, C)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
