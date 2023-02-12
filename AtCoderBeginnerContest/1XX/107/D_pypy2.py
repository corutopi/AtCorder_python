# 解説を参考に作成
# https://qiita.com/DaikiSuyama/items/7295f5160a51684554a7
# https://algo-logic.info/binary-indexed-tree/
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


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


def binary_search(ok, ng, solve):
    """2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    import math
    sorted_A = sorted(A)
    ok = 0
    ng = len(sorted_A)
    middle = math.ceil((N * (N + 1)) // 2 / 2)

    def search(mid):
        tmp_A = [1 if a >= sorted_A[mid] else -1 for a in A]
        sum_A = [0]
        for a in tmp_A:
            sum_A.append(sum_A[-1] + a)
        tmp_m = min(sum_A)
        up_A = [a - tmp_m + 1 for a in sum_A]
        bit = BinaryIndexedTree(max(up_A))
        over = 0
        bit.add(up_A[0], 1)
        for a in up_A[1:]:
            over += bit.sum(a)
            bit.add(a, 1)
        if over >= middle:
            return True
        else:
            return False

    print(sorted_A[binary_search(ok, ng, search)])


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str
    # N = 10 ** 5
    # A = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, A)
