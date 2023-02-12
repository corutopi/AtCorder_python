"""
解説と以下を参考に作成
    https://atcoder.jp/contests/abc199/submissions/22040886
    https://atcoder.jp/contests/abc199/submissions/22040875
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


class UnionFind:
    """
    下記から拝借
    https://note.nkmk.me/python-union-find/
    """

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(
            '{}: {}'.format(r, self.members(r)) for r in self.roots())


from decorator import stop_watch


@stop_watch
def solve(N, M, AB):
    graph_map = [[] for _ in range(N)]
    uf = UnionFind(N)
    for a, b in AB:
        graph_map[a - 1].append(b - 1)
        graph_map[b - 1].append(a - 1)
        uf.union(a - 1, b - 1)
    node_color = [0] * N

    # def dfs(index):
    #     if index == len(now_group):
    #         return 1
    #     c = [True] * 4
    #     for gm in graph_map[now_group[index]]:
    #         c[node_color[gm]] = False
    #     re = 0
    #     for i in range(1, 4):
    #         if c[i]:
    #             node_color[now_group[index]] = i
    #             re += dfs(index + 1)
    #             node_color[now_group[index]] = 0
    #     return re
    #
    # ans = 1
    # all_groups = list(uf.all_group_members().values())
    # for g in range(uf.group_count()):
    #     now_group = all_groups[g]
    #     node_color[all_groups[g][0]] = 1
    #     ans *= dfs(1) * 3
    # return ans

    def dfs1(v):
        order.append(v)
        for gg in graph_map[v]:
            if gg not in order:
                dfs1(gg)

    def dfs2(v):
        if v == len(order):
            return 1
        re = 0
        ban = set()
        for nv in graph_map[order[v]]:
            ban.add(color[nv])
        for c in range(1, 4):
            if c not in ban:
                color[order[v]] = c
                re += dfs2(v + 1)
                color[order[v]] = 0
        return re

    ans = 1
    root = uf.roots()
    for r in root:
        # order = uf.members(r)  # <- こっちだと tree_05.txt のケースが通らない。なんで？？
        order = []
        dfs1(r)
        color = [0] * N
        color[order[0]] = 1
        ans *= dfs2(1) * 3

    return ans


def checker(N, M, AB):
    graph_map = [[] for _ in range(N)]
    for a, b in AB:
        graph_map[a - 1].append(b - 1)
        graph_map[b - 1].append(a - 1)
    color = [0] * N

    def dfs(index):
        if index == N:
            flg = True
            for i in range(N):
                for gm in graph_map[i]:
                    if color[i] == color[gm]:
                        flg = False
                        break
                if not flg:
                    break
            return 1 if flg else 0
        re = 0
        for i in range(1, 4):
            color[index] = i
            re += dfs(index + 1)
        return re

    # print(dfs(0))
    return dfs(0)


if __name__ == '__main__':
    # N, M = map(int, input().split())
    # AB = [[int(i) for i in input().split()] for _ in range(M)]
    # print(solve(N, M, AB))
    # print(checker(N, M, AB))

    N, M = 20, 0
    AB = [[i, i + 1] for i in range(1, N)]
    print(AB)
    print(solve(N, M, AB))
    AB = [[1, i] for i in range(2, N + 1)]
    print(AB)
    print(solve(N, M, AB))
    AB = [[i, j] for i in range(1, N) for j in range(i + 1, N + 1)]
    print(AB)
    print(solve(N, M, AB))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # cnt = 0
    # while True:
    #     N = 8
    #     M = randint(0, N * (N - 1) // 2)
    #     AB = []
    #     AB_Sort = []
    #     for _ in range(M):
    #         a, b = 0, 0
    #         while True:
    #             a, b = randint(1, N), randint(1, N)
    #             if a == b: continue
    #             else:
    #                 aa, bb = min(a, b), max(a, b)
    #                 flg = True
    #                 for aaa, bbb in AB_Sort:
    #                     if aa == aaa and bb == bbb:
    #                         flg = False
    #                         break
    #                 if flg:
    #                     break
    #         AB.append([a, b])
    #         AB_Sort.append([min(a, b), max(a, b)])
    #     if solve(N, M, AB) != checker(N, M, AB):
    #         print(N, M)
    #         print(AB)
    #         print(solve(N, M, AB), checker(N, M, AB))
    #         break
    #     cnt += 1
    #     if cnt % 100 == 0:
    #         print('loop', cnt)
