# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABCD):
    graph = [[] for _ in range(N)]
    for a, b, c, d in ABCD:
        a = int(a)
        c = int(c)
        graph[a - 1].append(c - 1)
        graph[c - 1].append(a - 1)
    visited = [0] * N
    roop, straight = 0, 0
    for i in range(N):
        if visited[i]: continue
        q = deque([[i, -1]])
        flg = False
        while q:
            now, parent = q.popleft()
            if visited[now]:
                flg = True
                continue
            visited[now] = 1
            parent_flg = True
            for g in graph[now]:
                if g == parent and parent_flg:
                    parent_flg = False  # 2本でループしている場合のために親を除く
                    continue
                q.append([g, now])
        if flg:
            roop += 1
        else:
            straight += 1
    print(roop, straight)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABCD = [input().split() for _ in range(M)]
    solve(N, M, ABCD)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
