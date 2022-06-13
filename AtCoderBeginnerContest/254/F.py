"""
解説AC
"""
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


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


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
        res_l = self.default
        res_r = self.default
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res_l = self.func(res_l, self.tree[l])
                l += 1
            if r & 1:
                res_r = self.func(self.tree[r - 1], res_r)
            l >>= 1
            r >>= 1
        return self.func(res_l, res_r)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, A, B, query):
    st_A = SegTree([abs(A[i] - A[i + 1]) for i in range(N - 1)], gcd, 0)
    st_B = SegTree([abs(B[i] - B[i + 1]) for i in range(N - 1)], gcd, 0)
    for h1, h2, w1, w2 in query:
        h1 -= 1
        h2 -= 1
        w1 -= 1
        w2 -= 1
        tmp = A[h1] + B[w1]
        tmp = gcd(tmp, st_A.query(h1, h2)) if h1 != h2 else tmp
        tmp = gcd(tmp, st_B.query(w1, w2)) if w1 != w2 else tmp
        print(tmp)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, A, B, query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
