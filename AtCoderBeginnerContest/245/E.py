"""
解説を参考に作成.
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


def coordinate_compression(x, start=0):
    """整数のリストを座標圧縮したものを返す.デフォルトの最小値0.

    :param x: integer list
    :param start:
    :return:
    """
    xd = {v: i + start for i, v in enumerate(sorted(x))}
    return list(map(lambda d: xd[d], x))


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
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
def solve(N, M, A, B, C, D):
    empty_box = BinaryIndexedTree(N + M)
    choco_box_X = coordinate_compression(A + C, 1)
    choco_box_Y = coordinate_compression(B + D, 1)
    choco_box = [[choco_box_X[i], choco_box_Y[i], 0 if i < N else 1] for i in
                 range(N + M)]
    choco_box.sort()
    for i in range(N + M - 1, -1, -1):
        x, y, s = choco_box[i]
        if s == 1:
            empty_box.add(y, 1)
        else:
            if empty_box.sum_lr(y, empty_box.num) <= 0:
                # print('No')
                return 'No'

            def solver(s):
                return True if empty_box.sum_lr(y, s) > 0 else False

            empty_box.add(binary_search(empty_box.num, y - 1, solver), -1)

    # print('Yes')
    return 'Yes'


def solve_force(N, M, A, B, C, D):
    selected_box = [0] * M

    def dfs(x):
        if x == N:
            return True
        for m in range(M):
            if selected_box[m] == 1:
                continue
            if A[x] <= C[m] and B[x] <= D[m]:
                selected_box[m] = 1
                if dfs(x + 1):
                    return True
                selected_box[m] = 0
        return False

    return 'Yes' if dfs(0) else 'No'


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]
    print(solve(N, M, A, B, C, D))
    # print(solve_force(N, M, A, B, C, D))

    # N, M = 3, 3
    # A = [3, 8, 4]
    # B = [10, 8, 4]
    # C = [10, 7, 8]
    # D = [7, 5, 10]
    # print(solve(N, M, A, B, C, D))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     N, M = 3, 3
    #     A = random_ints(N, 1, 10)
    #     B = random_ints(N, 1, 10)
    #     C = random_ints(M, 1, 10)
    #     D = random_ints(M, 1, 10)
    #     if solve(N, M, A, B, C, D) != solve_force(N, M, A, B, C, D):
    #         print(solve(N, M, A, B, C, D))
    #         print(solve_force(N, M, A, B, C, D))
    #         print(A)
    #         print(B)
    #         print(C)
    #         print(D)
    #         break
