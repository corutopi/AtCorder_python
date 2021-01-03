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
def solve(N, M):
    if M < 0 or (N != 1 and N - 1 <= M):
        print(-1)
        return
    ans = []
    now = 1
    if 0 < M:
        ans.append([1, 10 ** 5 * 5])
        for m in range(M + 1):
            ans.append([2 + m * 2, 2 + m * 2 + 1])
        now = 10 ** 5 * 5 + 1
    while len(ans) < N:
        ans.append([now, now + 1])
        now += 2
    [print(' '.join([str(i) for i in j])) for j in ans]


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
