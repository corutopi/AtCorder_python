# 解説AC
# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
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
        while k <= self.num:
            self.tree[k] += x
            k += k & -k

    def sum(self, k):
        """
        1 ～ k までの合計
        :param k:
        :return:
        """
        re = 0
        while k > 0:
            re += self.tree[k]
            k -= k & -k
        return re

    def sum_lr(self, l, r):
        """
        sum of form l to r
        :param l: 1 <= l <= r
        :param r: l <= r <= self.num
        :return:
        """
        return self.sum(r) - self.sum(l - 1)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B):
    As = sorted(A)
    Bs = sorted(B)
    # 要素が一致しなければNo
    for a, b in zip(As, Bs):
        if a != b:
            print('No')
            return
    # 要素に重複があればYes
    for i in range(N - 1):
        if As[i] == As[i + 1]:
            print('Yes')
            return
    A_bit = BinaryIndexedTree(5000)
    B_bit = BinaryIndexedTree(5000)
    A_invers = 0
    B_invers = 0
    for i in range(N):
        a = A[i]
        A_invers += A_bit.sum(a)
        A_bit.add(a, 1)
        b = B[i]
        B_invers += B_bit.sum(b)
        B_bit.add(b, 1)
    print('Yes' if A_invers % 2 == B_invers % 2 else 'No')


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 5000
    # B = [i for i in range(1, N + 1)]
    # A = list(reversed(B))
    # solve(N, A, B)

    # # solve()
    # dict = {}
    # x = '1234'
    # for _ in range(10 ** 6):
    #     if dict.get(x, 0) == 0:
    #         dict[x] = 1
    #     t = randint(0, 1)
    #     m = [a for a in x]
    #     n = [a for a in x]
    #     n[t] = m[t + 2]
    #     n[t + 1] = m[t]
    #     n[t + 2] = m[t + 1]
    #     x = ''.join(n)
    # k = dict.keys()
    # k = sorted(k)
    # print(len(k))
    # for kk in k:
    #     print(kk)
