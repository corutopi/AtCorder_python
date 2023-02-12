# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, T, A, abc):
    from1_map = [[] for _ in range(N + 1)]
    to1_map = [[] for _ in range(N + 1)]
    for a, b, c in abc:
        from1_map[a].append([b, c])
        to1_map[b].append([a, c])

    from1_min = [inf] * (N + 1)
    from1_min[1] = 0
    hq = [[0, 1]]
    while hq:
        time, now = heappop(hq)
        if from1_min[now] < time: continue
        for i, t in from1_map[now]:
            if from1_min[i] < time + t: continue
            from1_min[i] = time + t
            heappush(hq, [time + t, i])

    to1_min = [inf] * (N + 1)
    to1_min[1] = 0
    hq = [[0, 1]]
    while hq:
        time, now = heappop(hq)
        if to1_min[now] < time: continue
        for i, t in to1_map[now]:
            if to1_min[i] < time + t: continue
            to1_min[i] = time + t
            heappush(hq, [time + t, i])

    ans = 0
    for i in range(1, N + 1):
        ans = max(ans, (T - from1_min[i] - to1_min[i]) * A[i - 1])
    print(ans)


if __name__ == '__main__':
    N, M, T = map(int, input().split())
    A = [int(i) for i in input().split()]
    abc = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, T, A, abc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
