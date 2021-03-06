# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
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
def solve(N, K, A):
    uf_row = UnionFind(N)
    uf_col = UnionFind(N)
    # grouping row
    for x in range(N - 1):
        for y in range(x + 1, N):
            flg = True
            for i in range(N):
                if A[x][i] + A[y][i] > K:
                    flg = False
                    break
            if flg:
                uf_row.union(x, y)
    # grouping col
    for x in range(N - 1):
        for y in range(x + 1, N):
            flg = True
            for i in range(N):
                if A[i][x] + A[i][y] > K:
                    flg = False
                    break
            if flg:
                uf_col.union(x, y)
    # calc ans
    ans = 1
    for gm in uf_row.all_group_members().values():
        for i in range(1, len(gm) + 1):
            ans *= i
            ans %= mod2
    for gm in uf_col.all_group_members().values():
        for i in range(1, len(gm) + 1):
            ans *= i
            ans %= mod2
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, K = 50, 2 * 50 ** 2
    # A = [[N * i + j for j in range(1, N + 1)] for i in range(N)]
    # solve(N, K, A)
