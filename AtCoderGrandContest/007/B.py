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
def solve(N, P):
    bit = BinaryIndexedTree(N)
    for i in range(N):
        bit.add(P[i], i)
    A = [i + bit.sum(i) for i in range(1, N + 1)]
    B = [i - (bit.sum(N - i) if i < N else 0) for i in range(N, 0, -1)]
    # C = []
    # for c in range(N, 0, -1):
    #     tmp = c - (bit.sum(N - c) if c < N else 0)
    #     C.append(tmp)
    min_b = abs(min(B)) + 1
    B = [b + min_b for b in B]
    return A, B
    # print(*A)
    # print(*B)


# def check(N, P, A, B):
#     AS = sorted(A)
#     BS = sorted(B, reverse=True)
#     for a1, a2 in zip(A, AS):
#         if a1 != a2:
#             return False
#     for b1, b2 in zip(B, BS):
#         if b1 != b2:
#             return False
#     PAB = [[P[i], A[i] + B[i]] for i in range(N)]
#     PAB.sort()
#     for i in range(N - 1):
#         if PAB[i][1] >= PAB[i + 1][1]:
#             return False
#     return True


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    A, B = solve(N, P)
    # print(check(N, P, A, B))
    print(' '.join([str(x) for x in A]))
    print(' '.join([str(x) for x in B]))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
