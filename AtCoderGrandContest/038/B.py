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


class BinaryIndexedTree:
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8] のlistを例とした場合、
    以下のような範囲での演算結果(sum)を配列に持つ。
        1: [1, 2, 3, 4, 5, 6, 7, 8]
        2: [1, 2, 3, 4]
        3: [1, 2]      [5, 6]
        4: [1]   [3]   [5]   [7]
    1 ～ r までの結果S(r)を、各層で必要な演算済みのデータを使うことで log(N) で計算できる.
    l ～ r までの結果は S(r) - S(l - 1) で同じくlog(N)計算できる.
    データ構造の作成は N*log(N).
    配列データは1始まりとして計算.
    長さ n + 1 (0 ~ n) の配列にデータを持ち, データ内の対象要素を l ~ r とすると, 配列の r 番目が格納先となる.
    また対象要素の数は r の LSB(Least Significant Bit) に一致する.

    転倒数の計算にも使える.
    """

    def __init__(self, n):
        """
        :param n: num of date.
        """
        self.num = n
        self.tree = [0] * (n + 1)

    def add(self, k, x):
        """
        :param k: [1, self.num]
        :param x: add num.
        :return: None
        """
        cnt = 0
        while k <= self.num:
            self.tree[k] += x
            k += k & -k
            cnt += 1
            if cnt % 100000 == 0:
                print('wow')

    def sum(self, k):
        """
        1 ～ k までの合計
        :param k:
        :return:
        """
        if not (1 <= k <= self.num):
            return 0
        re = 0
        cnt = 0
        while k > 0:
            re += self.tree[k]
            k -= k & -k
            cnt += 1
            if cnt % 100000 == 0:
                print('wow')
        return re

    def sum_lr(self, l, r):
        """
        sum of form l to r
        :param l: 1 <= l <= r
        :param r: l <= r <= self.num
        :return:
        """
        if not (1 <= l <= r <= self.num):
            return 0
        return self.sum(r) - self.sum(l - 1)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, P):
    if N == K:
        print(1)
        return
    bit = BinaryIndexedTree(N)
    ans = 1
    # 連続したK個が既に昇順になっていることの前計算
    isbig = [1 if P[i] > P[i + 1] else 0 for i in range(N - 1)]
    isbig_cs = [0]
    for ib in isbig:
        isbig_cs.append(isbig_cs[-1] + ib)
    default_flg = 0
    # 先頭からK個をbitに前計算
    for i in range(K):
        bit.add(P[i], 1)
    if isbig_cs[K - 1] - isbig_cs[0] == 0:
        default_flg = 1
    # 連続したK個をスライドして計算していく
    for i in range(K, N):
        out_num = P[i - K]
        in_num = P[i]
        bit.add(out_num, - 1)
        if bit.sum(out_num - 1) > 0 or bit.sum_lr(in_num + 1, N) > 0:
            if isbig_cs[i] - isbig_cs[i - K + 1] == 0 and default_flg == 0:
                ans += 1
                default_flg = 1
            elif isbig_cs[i] - isbig_cs[i - K + 1] > 0:
                ans += 1
        bit.add(in_num, 1)
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = [int(i) + 1 for i in input().split()]
    solve(N, K, P)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
