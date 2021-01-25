"""
解説と以下を参考に作成
https://drken1215.hatenablog.com/entry/2019/05/07/000200
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
def solve(H, W, N, sr, sc, S, T):
    l, r = 1, W
    u, d = 1, H
    S = [S[N - i - 1] for i in range(N)]
    T = [T[N - i - 1] for i in range(N)]

    if S[0] == 'L': l += 1
    if S[0] == 'R': r -= 1
    if S[0] == 'U': u += 1
    if S[0] == 'D': d -= 1

    for i in range(1, N):
        if T[i] == 'L': r = min(W, r + 1)
        if T[i] == 'R': l = max(1, l - 1)
        if S[i] == 'L': l += 1
        if S[i] == 'R': r -= 1
        if r < l:
            print('NO')
            return
        if T[i] == 'U': d = min(H, d + 1)
        if T[i] == 'D': u = max(1, u - 1)
        if S[i] == 'U': u += 1
        if S[i] == 'D': d -= 1
        if d < u:
            print('NO')
            return

    ans = 'NO'
    if l <= sc <= r and u <= sr <= d:
        ans = 'YES'

    print(ans)


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    sr, sc = map(int, input().split())
    S = input()
    T = input()
    solve(H, W, N, sr, sc, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
