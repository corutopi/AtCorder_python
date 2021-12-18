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
def solve(R, C, K, s):
    m = [[0 if ss == 'o' else 1 for ss in s[r]] for r in range(R)]
    cs_m = [[]]
    for r in range(R):
        t = [0]
        for c in range(C):
            t.append(t[-1] + m[r][c])
        cs_m.append(t)

    ans = 0
    for x, y in ((r, c) for r in range(R) for c in range(C)):
        if not K <= x <= R - K + 1 or not K <= y <= C - K + 1:
            continue
        for n in range(-(K - 1), K):
            if cs_m[x + n][y + (K - 1 - abs(n))] \
                    - cs_m[x + n][y - (K - 1 - abs(n)) - 1] > 0:
                break
        else:
            ans += 1
    print(ans)


if __name__ == '__main__':
    R, C, K = map(int, input().split())
    s = [input() for _ in range(R)]
    solve(R, C, K, s)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # R, C, K = 500, 500, randint(2, 10)
    # s = [random_str(C, 'oooooox') for _ in range(R)]
    # solve(R, C, K, s)
