"""
解説を参考に作成
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    uf = UnionFind(H + W)
    uf.union(0, H)
    uf.union(0, H + W - 1)
    uf.union(H - 1, H)
    uf.union(H - 1, H + W - 1)
    for h, w in ((h, w) for w in range(W) for h in range(H)):
        if S[h][w] == '#':
            uf.union(h, H + w)
    ans_H = sum([1 for ns in uf.all_group_members().values() if min(ns) < H])
    ans_W = sum([1 for ns in uf.all_group_members().values() if max(ns) >= H])
    print(min(ans_H, ans_W) - 1)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 1000, 1000
    # S = [random_str(W, '...................................#') for _ in range(H)]
    # solve(H, W, S)
