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


def inverse(a, p):
    """逆元"""
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


def dev_mod(a, b, mod):
    """a(= A % mod) / b を mod で割った余り"""
    return (a * inverse(b, mod)) % mod


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    sort_A = sorted(A)
    cmp_map = {sort_A[0]: 1}
    for i in range(1, N):
        if sort_A[i - 1] == sort_A[i]: continue
        cmp_map[sort_A[i]] = cmp_map[sort_A[i - 1]] + 1
    cmp_A = [cmp_map[a] for a in A]

    st = SegTree([0] * (N + 1), lambda x, y: (x + y) % mod2, 0)

    m2 = [1]
    for _ in range(N):
        m2.append(m2[-1] * 2 % mod2)
    m2mod = [dev_mod(1, m2[0], mod2)]
    for _ in range(N):
        m2mod.append(dev_mod(m2mod[-1], 2, mod2))

    B = []
    for j, a in enumerate(cmp_A, 1):
        B.append(st.query(0, a + 1))
        st.update(a, st.element(a) + m2mod[j])
        # if j % 100000 == 0:
        #     print(j)

    print(sum([B[i] * m2[i] % mod2 for i in range(N)]) % mod2)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 3 * 10 ** 5
    # # N = 1000
    # A = random_ints(N, 1, 10 ** 9)
    # solve(N, A)
