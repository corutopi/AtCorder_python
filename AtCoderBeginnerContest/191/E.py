# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
import heapq
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABC):
    load_map = [[] for _ in range(N + 1)]
    for a,b,c in ABC:
        load_map[a].append((c, b))

    ans = [0] * (N + 1)
    for i in range(1, N + 1):
        time = [inf] * (N + 1)
        hq = [(0, i)]
        while hq:
            t, n = heapq.heappop(hq)
            if time[n] <= t:
                continue
            if t != 0:
                time[n] = t
            for new_t, new_n in load_map[n]:
                if t + new_t < time[new_n]:
                    heapq.heappush(hq, (t + new_t, new_n))
        ans[i] = time[i] if time[i] != inf else -1

    [print(i) for i in ans[1:]]


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, ABC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, M = 2000, 2000
    # ABC = [[randint(1, 2000), randint(1, 2000), randint(1, 10 ** 5)] for _ in range(M)]
    # solve(N, M, ABC)
