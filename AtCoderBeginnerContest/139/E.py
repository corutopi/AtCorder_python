# 解説を参考に作成
import sys

sys.setrecursionlimit(10 ** 6)
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
def solve(N, A):
    XXX = 20
    dgmap = [[] for _ in range(2 ** XXX)]  # 有向グラフ (directed graph
    # 有向グラフの作成
    for i, j in ((i, j) for i in range(N) for j in range(N - 2)):
        x = A[i][j]  # i の j 番目の対戦相手
        a, b = max(i, x), min(i, x)  # 大小をそろえて対戦を同じ数字で扱えるようにする
        n = (a << 10) + b  # a と b の対戦を表す数字
        x2 = A[i][j + 1]  # i の j + 1 番目(xの次)の対戦相手
        a2, b2 = max(i, x2), min(i, x2)
        n2 = (a2 << 10) + b2
        # 辺を追加(n2 の対戦は n が終わってからでないと実施できない)
        dgmap[n].append([n2, False])  # 再帰呼び出し時に使用済みかどうか判定して閉路を見つける
    # 探索
    ans = 0
    deapest = [-1] * 2 ** 20
    for p in range(2 ** 20):
        if deapest[p] >= 0: continue

        def dfs(now):
            if len(dgmap[now]) == 0:
                # 出次数0の場合は深さ1とする
                deapest[now] = 1
                return deapest[now]
            re = 0
            for dm in dgmap[now]:
                # 使用済みの経路を使おうとしている場合は閉路とみなす
                if dm[1]:
                    return -1
                dm[1] = True
                tmp = deapest[dm[0]] if deapest[dm[0]] >= 0 else dfs(dm[0])
                if tmp == -1:
                    return -1
                re = max(re, tmp + 1)
                dm[1] = False
            deapest[now] = re
            return deapest[now]

        dfs(p)
        if deapest[p] == -1:
            print(-1)
            return
    print(max(deapest))


if __name__ == '__main__':
    N = int(input())
    A = [[int(i) - 1 for i in input().split()] for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
