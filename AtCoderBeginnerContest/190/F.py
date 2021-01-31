# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(N, A):
    A = [a + 1 for a in A]
    bit = BinaryIndexedTree(N + 1)
    inversions = [0] * (N + 1)
    for a in A:
        inversions[a] = bit.sum_lr(a + 1, N + 1)
        bit.add(a, 1)
    # print(inversions)

    bit2 = BinaryIndexedTree(N + 1)
    anses = [sum(inversions)]

    for i in range(N - 1, 0, -1):
        tmp = anses[-1]
        a = A[i]
        tmp -= inversions[a]  # もともとの転倒数
        tmp -= bit2.sum_lr(a + 1, N + 1)  # 直前までに右端→左端に移されたことで増えた転倒数
        tmp += a - 1  # 右端→左端に移されることで増える転倒数
        anses.append(tmp)  # 現在の転倒数として記録
        bit2.add(a, 1)  # 右端→左端に移した数字の記録

    [print(ans) for ans in anses[0:1] + list(reversed(anses[1:]))]


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint, shuffle
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 3 * 10 ** 5
    # A = [i for i in range(N)]
    # shuffle(A)
    # solve(N, A)
