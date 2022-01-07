# 解説を参考に作成
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
        """
        make lonely group 0 to (n - 1).

        :param n:
        """
        self._n = n
        self._parents = [-1] * n
        self._group_count = n

    def find(self, x):
        """
        return the number of representatives of the group to which x belongs.

        :param x:
        :return:
        """
        if self._parents[x] < 0:
            return x
        else:
            self._parents[x] = self.find(self._parents[x])
            return self._parents[x]

    def union(self, x, y):
        """
        join the group to which x belongs and the group to which y belongs.

        :param x:
        :param y:
        :return:
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if x > y:
            x, y = y, x

        self._parents[x] += self._parents[y]
        self._parents[y] = x
        self._group_count -= 1

    def size(self, x):
        """
        return member num of group to which x belongs.

        :param x:
        :return:
        """
        return -self._parents[self.find(x)]

    def same(self, x, y):
        """
        return True if x is the same group as y else False.

        :param x:
        :param y:
        :return:
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        return members of the same group as x.

        :param x:
        :return:
        """
        root = self.find(x)
        return [i for i in range(self._n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self._parents) if x < 0]

    def group_count(self):
        return self._group_count

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(
            '{}: {}'.format(r, self.members(r)) for r in self.roots())


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, C, Query):
    uf = UnionFind(N + 1)
    d = [{}] + [{c: 1} for c in C]
    for q, r, s in Query:
        if q == 1:
            if uf.same(r, s): continue
            rp, sp = uf.find(r), uf.find(s)
            rp, sp = (sp, rp) if len(d[rp]) < len(d[sp]) else (rp, sp)
            for key, value in d[sp].items():
                d[rp].setdefault(key, 0)
                d[rp][key] += value
            d[min(rp, sp)] = d[rp]
            d[max(rp, sp)] = {}
            uf.union(r, s)
        elif q == 2:
            print(d[uf.find(r)].get(s, 0))


if __name__ == '__main__':
    N, Q = map(int, input().split())
    C = [int(i) for i in input().split()]
    Query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, C, Query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, Q = 10, 1000
    # cnum = 2
    # C = random_ints(N, 1, cnum)
    # Query = []
    # for _ in range(Q):
    #     a = int(random_str(1, '1112'))
    #     if a == 1:
    #         b, c = randint(1, N), randint(1, N)
    #     else:
    #         b, c = randint(1, N), randint(1, cnum)
    #     Query.append([a, b, c])
    # C = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    # Query = [[1, 1, 2],
    #          [1, 4, 3],
    #          [2, 1, 1],
    #          [2, 3, 1],
    #          [1, 2, 3],
    #          [2, 3, 2],]
    # solve(N, Q, C, Query)
