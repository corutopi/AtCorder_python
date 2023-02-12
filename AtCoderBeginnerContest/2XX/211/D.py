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
def solve(N, M, AB):
    loadmap = [[] for _ in range(N)]
    for a, b in AB:
        loadmap[a].append(b)
        loadmap[b].append(a)
    min_pattern = [[inf, 0] for _ in range(N)]
    min_pattern[0] = [0, 1]
    dq = deque([0])
    while dq:
        now = dq.popleft()
        min_pattern[now][1] %= mod
        next_time = min_pattern[now][0] + 1
        for n in loadmap[now]:
            if min_pattern[n][0] > next_time:
                min_pattern[n] = [next_time, min_pattern[now][1]]
                dq.append(n)
            elif min_pattern[n][0] == next_time:
                min_pattern[n][1] += min_pattern[now][1]

    print(min_pattern[-1][1])


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    AB = [[int(i) - 1 for i in input().split()] for _ in range(M)]
    solve(N, M, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
