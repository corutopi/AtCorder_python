# 解説などを参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

class SegTree:
    # 参考
    # https://algo-logic.info/segment-tree/#toc_id_1
    # https://qiita.com/takayg1/items/c811bd07c21923d7ec69
    # --イメージ--------
    #  1  1  1  1  1  1  1  1
    #  2  2  2  2  3  3  3  3
    #  4  4  5  5  6  6  7  7
    #  8  9 10 11 12 13 14 15
    # ------------------
    # 同じ番号の範囲すべての func 結果を配列に持つ
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
def solve(N, K, A):
    import math
    ma = max(A) + 1
    dp = [0] * (max(A) + 1)
    st = SegTree(dp, lambda x, y: max(x, y), -(math.inf))
    for a in A:
        # print(st.query(a - K, a + K + 1))

        l = max(0, a - K)
        r = min(ma, a + K + 1)

        st.update(a, st.query(l, r) + 1)
    print(st.query(0, max(A) + 1))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    solve(N, K, A)

    # # test
    # from random import randint
    # from func import random_str
    #
    # N, K = 300000, 300000
    # A = [i for i in range(1, N + 1)]
    # print(N, K)
    # print(A)
    # print()
    # solve(N, K, A)
