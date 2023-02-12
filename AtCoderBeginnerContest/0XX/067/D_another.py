# import sys
#
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def minimum_load(tree_map, start, end):
    """
    グラフの start から end までの最短の道順を検索する
    :param tree_map: [[], [1と行き来できるノード], [2と行き来できるノード], ...]
    :param start:
    :param end:
    :return: node_list[start, a1, a2, ... , end]
    """
    from collections import deque
    node_num = len(tree_map)
    parent_map = [-1] * node_num
    # make parent_map
    dq = deque([[end, -1]])
    while dq:
        now, parent = dq.popleft()
        parent_map[now] = parent
        if now == start:
            break
        for t in tree_map[now]:
            if t == parent:
                continue
            dq.append([t, now])
    # make load
    re = []
    now = start
    while True:
        re.append(now)
        if now == end:
            break
        now = parent_map[now]
    return re


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

    FtoS = minimum_load(tree_map, 1, N)

    # decide two top
    f_top = FtoS[ceil(len(FtoS) / 2) - 1]
    s_top = FtoS[ceil(len(FtoS) / 2) - 1 + 1]

    # count tops two tree, and winner is have more than top
    tree_map[f_top].remove(s_top)
    tree_map[s_top].remove(f_top)

    def top_count(node):
        dq = deque([[node, 0]])
        re = 0
        while dq:
            now, parent = dq.popleft()
            re += 1
            for t in tree_map[now]:
                if t == parent:
                    continue
                dq.append([t, now])
        return re

    f_num = top_count(f_top)
    s_num = top_count(s_top)

    print('Fennec' if f_num > s_num else 'Snuke')


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
    # solve(10 ** 5, tt.make_tree_data(10 ** 5))
    # # N = 7
    # # ab = [[1, 2], [1, 7], [4, 7], [3, 7], [2, 5], [2, 6]]
    # # solve(N, ab)
