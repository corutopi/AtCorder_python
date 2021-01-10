# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, ab):
    from math import ceil

    tree_map = [[] for _ in range(N + 1)]
    for a, b in ab:
        tree_map[a].append(b)
        tree_map[b].append(a)

    fs_map = ['0'] * (N + 1)
    depth_map = [0] * (N + 1)
    dq = deque([[1, 0, 0]])
    while dq:
        now, parent, depth = dq.popleft()
        depth_map[now] = depth
        for t in tree_map[now]:
            if t == parent:
                continue
            dq.append([t, now, depth + 1])
    dq = deque([[N, 0, 0]])
    while dq:
        now, parent, depth = dq.popleft()
        fs_map[now] = 'S' if depth_map[now] > depth else 'F'
        for t in tree_map[now]:
            if t == parent:
                continue
            dq.append([t, now, depth + 1])
    print('Fennec' if fs_map.count('F') > fs_map.count('S') else 'Snuke')


if __name__ == '__main__':
    N = int(input())
    ab = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, ab)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # solve(10 ** 5, tt.make_tree_data(10 ** 5, 1))
    # N = 7
    # ab = [[1, 2], [1, 7], [4, 7], [3, 7], [2, 5], [2, 6]]
    # solve(N, ab)
