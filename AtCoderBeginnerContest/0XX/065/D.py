# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

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

        if self._parents[x] > self._parents[y]:
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
def solve(N, XY):
    road = []
    IXY = [[i] + XY[i] for i in range(N)]
    IXY.sort(key=lambda x: x[1])
    for j in range(N - 1):
        road.append([IXY[j][0], IXY[j + 1][0], abs(IXY[j][1] - IXY[j + 1][1])])
    IXY.sort(key=lambda x: x[2])
    for j in range(N - 1):
        road.append([IXY[j][0], IXY[j + 1][0], abs(IXY[j][2] - IXY[j + 1][2])])
    road.sort(key=lambda x: x[2])
    uf = UnionFind(N)
    ans = 0
    for i, j, c in road:
        if uf.same(i, j): continue
        ans += c
        uf.union(i, j)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
