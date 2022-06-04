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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, AB, Q, XK):
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    for x, k in XK:
        x -= 1
        visited = dict()
        dq = deque([[x, 0]])
        visited[x] = 1
        ans = x + 1
        while dq:
            now, depth = dq.popleft()
            if depth == k: continue
            for g in graph[now]:
                if visited.get(g, 0) == 1: continue
                visited[g] = 1
                ans += g + 1
                dq.append([g, depth + 1])
        print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    Q = int(input())
    XK = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, M, AB, Q, XK)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 150000
    # M = 300000
    # AB = tt.make_tree_data(N, 3)
    # Q = 10000
    # XK = [[randint(1, N), 3] for _ in range(Q)]
    # solve(N, M, AB, Q, XK)
