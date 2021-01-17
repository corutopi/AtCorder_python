"""
解説を参考に作成
"""
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
def solve(N, W, wv):
    w_base = wv[0][0]
    vs = [[], [], [], []]
    for w, v in wv:
        vs[abs(w_base - w)].append(v)

    for i in range(4):
        vs[i].sort(reverse=True)

    vs_cumsum = [[0], [0], [0], [0]]
    for i in range(len(vs_cumsum)):
        for j in range(len(vs[i])):
            vs_cumsum[i].append(vs_cumsum[i][-1] + vs[i][j])

    ans = 0
    for a in range(len(vs_cumsum[0])):
        for b in range(len(vs_cumsum[1])):
            for c in range(len(vs_cumsum[2])):
                for d in range(len(vs_cumsum[3])):
                    if W < (a + b + c + d) * w_base + b * 1 + c * 2 + d * 3:
                        continue
                    ans = max(ans,
                              vs_cumsum[0][a] + vs_cumsum[1][b] +
                              vs_cumsum[2][c] + vs_cumsum[3][d])
    print(ans)


if __name__ == '__main__':
    N, W = map(int, input().split())
    wv = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, W, wv)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
