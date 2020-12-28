# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7


class SegTree:
    """
    セグメントツリー
    参考:
        https://algo-logic.info/segment-tree/#toc_id_1
        https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    --イメージ--------
     1  1  1  1  1  1  1  1
     2  2  2  2  3  3  3  3
     4  4  5  5  6  6  7  7
     8  9 10 11 12 13 14 15  <- ここに配列の素の値が入る
    ------------------
    同じ番号の列すべての func 結果を配列に持つ
    """

    def __init__(self, elm, func, default):
        """
        :param elm: 配列
        :param func: 操作関数(f(x, y))
        :param default: 単位元
        """
        # create val
        self.num = 1 << (len(elm) - 1).bit_length()
        self.func = func
        self.tree = [default] * 2 * self.num
        self.default = default
        # update leaf
        for i in range(len(elm)):
            self.tree[self.num + i] = elm[i]
        # update nodes
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def element(self, k):
        """
        要素の取得
        :param k: elm の要素番号
        :return:
        """
        return self.tree[self.num + k]

    def update(self, k, x):
        """
        要素k の値を x に更新する
        :param k: elm の要素番号
        :param x:
        :return:
        """
        k = self.num + k
        self.tree[k] = x
        while k > 1:
            k = k // 2
            self.tree[k] = self.func(self.tree[k * 2], self.tree[k * 2 + 1])

    def query(self, l, r):
        """
        [l, r) の結果を取得する
        :param l: 0 始まりで指定する
        :param r:
        :return:
        """
        res = self.default
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.func(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S, Q, Query):
    SS = [set([s]) for s in S]
    segtree = SegTree(SS, lambda x, y: x.union(y), set())
    for a, b, c in Query:
        if a == 1:
            segtree.update(b - 1, {c})
        else:
            print(len(segtree.query(b - 1, c)))


if __name__ == '__main__':
    N = int(input())
    S = input()
    Q = int(input())
    Query = [input().split() for _ in range(Q)]
    for q in Query:
        q[0] = int(q[0])
        if q[0] == 1:
            q[1] = int(q[1])
        else:
            q[1] = int(q[1])
            q[2] = int(q[2])
    solve(N, S, Q, Query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 5 * 10 ** 5
    # S = random_str(N, string.ascii_lowercase)
    # Q = 20000
    # Query = []
    # for _ in range(Q):
    #     a = randint(1, 2)
    #     if a == 1:
    #         b = randint(1, N)
    #         c = random_str(1, string.ascii_lowercase)
    #     else:
    #         b = randint(1, N)
    #         c = randint(1, N)
    #         b, c = min(b, c), max(b, c)
    #     Query.append([a, b, c])
    # solve(N, S, Q, Query)
