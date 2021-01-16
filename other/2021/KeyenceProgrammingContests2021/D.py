"""
解説と下記を参考に作成.
https://twitter.com/kyopro_friends/status/1350448936213889025
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def hadamard_matrix(k):
    """
    アダマール行列を生成する.
    シルベスターの生成法を採用.
    参考:
        https://ja.wikipedia.org/wiki/アダマール行列

    :param k: 次元を表す指数. 2 ** k 次元のアダマール行列が生成される.
    :return: 1, -1 で構成された2次元配列
    """
    if k == 0:
        return [[1]]
    if k == 1:
        return [[1, 1],
                [1, -1]]
    H = hadamard_matrix(k - 1)
    H_ = [[-i for i in h] for h in H]
    HH = [H[i] + H[i] for i in range(len(H))] + \
         [H[i] + H_[i] for i in range(len(H))]
    return HH


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    i_c = {1: 'A', -1: 'B'}
    H = hadamard_matrix(N)
    print(len(H) - 1)
    for h in H[1:]:
        print(''.join([i_c[hi] for hi in h]))


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
