# 解説を参考に作成
# https://atcoder.jp/contests/acl1/submissions/17325730 を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque


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
def solve(N, XY):
    XY2 = sorted(XY)
    y_stack = [300000]  # yを降順に記録
    x_stack = [-1]  # yに対応するx(-1)の値を記録
    uf = UnionFind(N)
    for i in range(N):
        y = XY2[i][1]
        minY = min(y_stack[-1], y)  # 既存のyの最小値と比較して小さいほうを記録
        while y_stack[-1] < y:
            # 既存yの方が小さければ結合.以降,降順に並んでるので大きさが逆転するまで結合し続ける
            uf.union(i, x_stack.pop())
            y_stack.pop()
        # 結合結果の中で最小のy,xをstackに追加(結合した要素はすべてpopしているので)
        y_stack.append(minY)
        x_stack.append(i)
    # ソートする前の配列でprint. UnionFindはxでソートして作成しているのでx(-1)の要素のsizeを取得する
    [print(uf.size(x - 1)) for x, y in XY]


if __name__ == '__main__':
    # S = input()
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint, shuffle
    # from func import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # X = [i for i in range(1, N + 1)]
    # Y = [i for i in range(1, N + 1)]
    # shuffle(X)
    # shuffle(Y)
    # XY = [[X[i], Y[i]] for i in range(N)]
    # solve(N, XY)
