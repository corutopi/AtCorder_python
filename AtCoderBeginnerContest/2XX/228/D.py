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
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        return the number of representatives of the group to which x belongs.

        :param x:
        :return:
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

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

        # if self.parents[x] < self.parents[y]:
        #     x, y = y, x
        x, y = max(x, y), min(x, y)

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        return member num of group to which x belongs.

        :param x:
        :return:
        """
        return -self.parents[self.find(x)]

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
N = 2 ** 20


def solve(Q, tx):
    A = [-1] * N
    uf = UnionFind(N)
    ans = []
    for t, x in tx:
        if t == 1:
            if A[x % N] == -1:
                A[x % N] = x
                if x % N != N - 1:
                    uf.union(x % N, (x + 1) % N)
            else:
                p = uf.find(x % N)
                if p == N - 1 and A[p] != -1:
                    p = uf.find(0)
                A[p] = x
                if p != N - 1:
                    uf.union(p % N, (p + 1) % N)
        else:
            print(A[x % N])
            # ans.append(A[x % N])
        # print(t, uf.find(t))
    # return ans


def solve2(Q, tx):
    A = [-1] * N
    ans = []
    for t, x in tx:
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            # print(A[x % N])
            ans.append(A[x % N])
    return ans


if __name__ == '__main__':
    Q = int(input())
    tx = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(Q, tx)

    # # test
    # from random import randint, sample
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # Q = 0
    #
    # while True:
    #     ins = [[1, randint(0, N * 3)] for _ in range(N)]
    #     dsp = [[2, randint(0, N * 3)] for _ in range(N)]
    #     s = sample(ins + dsp, N * 2)
    #     a = solve(Q, s)
    #     b = solve2(Q, s)
    #     if a != b:
    #         print(s)
    #         print(a)
    #         print(b)
    #         break
