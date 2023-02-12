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
        self.tree = [default()] * 2 * self.num
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
        res_l = self.default()
        res_r = self.default()
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
def solve(N, Q, S, TLR):
    S_x = [[0 if s == '(' else -1,
            1 if s == '(' else -1] for s in S]

    def default():
        return [0, 0]

    def new_set(x, y):
        return [min(x[0], x[1] + y[0]), x[1] + y[1]]

    st = SegTree(S_x, new_set, default)
    for t, l, r in TLR:
        l -= 1
        r -= 1
        if t == 1:
            S_x[l], S_x[r] = S_x[r], S_x[l]
            st.update(l, S_x[l])
            st.update(r, S_x[r])
        else:
            print('Yes' if st.query(l, r + 1) == [0, 0] else 'No')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    TLR = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, S, TLR)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
