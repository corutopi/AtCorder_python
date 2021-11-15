# 解説を参考に作成
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
def solve(M, uv, p):
    min_dict = {}
    graph_map = [[] for _ in range(10)]
    for u, v in uv:
        graph_map[u].append(v)
        graph_map[v].append(u)
    s = '0' + '9' * 9
    for i, q in enumerate(p, 1):
        s = s[:q] + str(i) + s[q + 1:]
    min_dict[s] = 0
    dq = deque([s])
    while dq:
        now = dq.popleft()
        if now == '0123456789': break
        for i in range(10):
            if now[i] != '9': continue
            for gm in graph_map[i]:
                nxt = now.translate(str.maketrans('9' + str(now[gm]),
                                                  str(now[gm]) + '9'))
                if min_dict.get(nxt, 0) == 0:
                    min_dict[nxt] = min_dict[now] + 1
                    dq.append(nxt)
    print(min_dict.get('0123456789', -1))


if __name__ == '__main__':
    M = int(input())
    uv = [[int(i) for i in input().split()] for _ in range(M)]
    p = [int(i) for i in input().split()]
    solve(M, uv, p)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
