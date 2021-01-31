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
def solve(N, S):
    graph = [[] for _ in range(N)]
    ge = ((i, j) for i in range(N) for j in range(i))
    for i, j in ge:
        if S[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)
    ans = -1
    for top in range(N):
        V = [[] for _ in range(N)]
        checked = [-2] * N
        dq = deque([[top, 0]])
        flg = True
        checked[top] = 0
        while dq:
            now, v = dq.popleft()
            V[v].append(now)
            for g in graph[now]:
                if abs(v - checked[g]) == 1:
                    continue
                elif checked[g] >= 0:
                    flg = False
                    break
                dq.append([g, v + 1])
                checked[g] = v + 1
        if flg:
            ans = max(ans, max(checked) + 1)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [[int(i) for i in input()] for _ in range(N)]
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
