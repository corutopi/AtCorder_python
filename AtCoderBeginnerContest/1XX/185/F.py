# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
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
        return self.tree[self.num + k]

    def update(self, k, x):
        k = self.num + k
        self.tree[k] = x
        while k > 1:
            k = k // 2
            self.tree[k] = self.func(self.tree[k * 2], self.tree[k * 2 + 1])

    def query(self, l, r):
        """
        [l, r) の結果を取得する
        :param l:
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
def solve(N, Q, A, TXY):
    def func(x, y):
        return x ^ y
    seg = SegTree(A, func, 0)

    for t, x, y in TXY:
        if t == 1:
            seg.update(x - 1, seg.element(x - 1) ^ y)
        elif t == 2:
            print(seg.query(x - 1, y))


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    TXY = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, A, TXY)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
