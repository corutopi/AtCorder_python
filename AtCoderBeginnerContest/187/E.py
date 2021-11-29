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
def solve(N, AB, Q, TEX):
    tree = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree[a].append(b)
        tree[b].append(a)
    top = 0
    for i in range(N + 1):
        if len(tree[i]) == 1:
            top = i
            break
    # 階層を決める
    depth = [-1] * (N + 1)
    dq = deque([[top, 0]])
    while dq:
        now, d = dq.popleft()
        depth[now] = d
        for t in tree[now]:
            if depth[t] < 0:
                dq.append([t, d + 1])
    # 上に加算する値と下に加算する値をまとめる
    top_rlt = 0
    plus = [0] * (N + 1)
    minus = [0] * (N + 1)
    for t, e, x in TEX:
        a, b = AB[e - 1]
        if t == 2:
            a, b = b, a
        if depth[a] < depth[b]:
            minus[b] += x
            top_rlt += x
        else:
            plus[a] += x
    # top から順に頂点毎の値を計算する
    ans = [-1] * (N + 1)
    dq = deque([[top, top_rlt]])
    while dq:
        now, rlt = dq.popleft()
        rlt += plus[now]
        rlt -= minus[now]
        ans[now] = rlt
        for t in tree[now]:
            if ans[t] < 0:
                dq.append([t, rlt])
    [print(a) for a in ans[1:]]


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    Q = int(input())
    TEX = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, AB, Q, TEX)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints, make_tree_data
    # N = 2 * 10 ** 5
    # AB = make_tree_data(N)
    # Q = 2 * 10 ** 5
    # TEX = [[randint(1, 2),
    #         randint(1, N - 1),
    #         randint(1, 10 ** 9)] for _ in range(Q)]
    # solve(N, AB, Q, TEX)
