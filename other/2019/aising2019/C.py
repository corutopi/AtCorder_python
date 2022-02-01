# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    ans = 0
    S = ['*' * (W + 2)] + \
        ['*' + s + '*' for s in S] + \
        ['*' * (W + 2)]
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    for h, w in ((h, w) for h in range(1, H + 1) for w in range(1, W + 1)):
        if visited[h][w]: continue
        visited[h][w] = 1
        white, black = 0, 0
        dq = deque([[h, w]])
        while dq:
            nh, nw = dq.popleft()
            color = S[nh][nw]
            if S[nh][nw] == '#':
                black += 1
            elif S[nh][nw] == '.':
                white += 1

            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if visited[nh + x][nw + y] == 0 and \
                        S[nh + x][nw + y] != color and \
                        S[nh + x][nw + y] != '*':
                    dq.append([nh + x, nw + y])
                    visited[nh + x][nw + y] = 1
        ans += white * black

    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 400, 400
    # S = [random_str(W, '#.') for _ in range(H)]
    # solve(H, W, S)
