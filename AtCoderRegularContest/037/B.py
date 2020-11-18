# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, uv):
    ans = 0
    tree_map = [[] for _ in range(N + 1)]
    for u, v in uv:
        tree_map[u].append(v)
        tree_map[v].append(u)
    visit_flg = [0] * (N + 1)

    def is_tree(top):
        dq = deque([[top, 0]])
        re = 1
        while dq:
            now, parent = dq.pop()
            visit_flg[now] = 1
            for t in tree_map[now]:
                if t == parent:
                    continue
                if visit_flg[t] == 1:
                    re = 0
                    break
                dq.append([t, now])
            if re == 0:
                break
        return re

    for i in range(1, N + 1):
        if visit_flg[i] == 0:
            ans += is_tree(i)

    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    uv = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uv)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
