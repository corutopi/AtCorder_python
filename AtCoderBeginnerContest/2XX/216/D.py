# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# import string

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def have_close_road(graph):
    node_num = len(graph)
    parent_num = [0] * node_num
    parent_flg = [0] + [1] * (node_num - 1)
    for g in graph:
        for n in g:
            parent_num[n] += 1
            parent_flg[n] = 0

    remain_flg = [0] + [1] * (node_num - 1)
    for i in range(1, node_num):
        if parent_flg[i] == 0:
            continue
        stack = [i]
        while stack:
            now = stack.pop(-1)
            remain_flg[now] = 0
            for j in graph[now]:
                parent_num[j] -= 1
                if parent_num[j] == 0:
                    stack.append(j)

    return False if sum(remain_flg) == 0 else True


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, a):
    tree = [set([]) for _ in range(N + 1)]
    for ai in a:
        for i in range(len(ai) - 1):
            tree[ai[i]].add(ai[i + 1])
    print('No' if have_close_road(tree) else 'Yes')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in range(M * 2)][1::2]
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, M, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
