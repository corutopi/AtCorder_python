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
def solve(H, W, Q, q):
    mass = [[0] * (W + 2) for _ in range(H + 2)]
    uf = UnionFind(H * W + 1)
    for qq in q:
        pattern = qq[0]
        if pattern == 1:
            r, c = qq[1:]
            mass[r][c] = 1
            if mass[r - 1][c] == 1:
                # up
                uf.union(mass_num(r, c, W), mass_num(r - 1, c, W))
            if mass[r + 1][c] == 1:
                # down
                uf.union(mass_num(r, c, W), mass_num(r + 1, c, W))
            if mass[r][c - 1] == 1:
                # left
                uf.union(mass_num(r, c, W), mass_num(r, c - 1, W))
            if mass[r][c + 1] == 1:
                # right
                uf.union(mass_num(r, c, W), mass_num(r, c + 1, W))
        elif pattern == 2:
            r1, c1, r2, c2 = qq[1:]
            if mass[r1][c1] == mass[r2][c2] == 1 and \
                    uf.same(mass_num(r1, c1, W), mass_num(r2, c2, W)):
                print('Yes')
            else:
                print('No')


def mass_num(r, c, W):
    return W * (r - 1) + c


if __name__ == '__main__':
    H, W = map(int, input().split())
    Q = int(input())
    q = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(H, W, Q, q)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     H, W = randint(1, 20), randint(1, 20)
    #     Q = randint(1, 10)
    #     q = []
    #     for _ in range(Q):
    #         q1 = randint(1, 10)
    #         if q1 <= 9:
    #             q.append([1, randint(1, H), randint(1, W)])
    #         else:
    #             q.append([2,
    #                       randint(1, H), randint(1, W),
    #                       randint(1, H), randint(1, W)])
    #     print(H, W, Q, q)
    #     solve(H, W, Q, q)
