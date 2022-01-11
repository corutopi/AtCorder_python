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


class FermatCmb:
    """フェルマー小定理を使用した順列, 組み合わせ計算
    max_num = 10 ** 6 で 0.58 sec
    """

    def __init__(self, max_num, mod):
        """
        :param max_num: max n of nCk
        :param mod: any prime number
        """
        self.max_num = max_num
        self.mod = mod
        self.fact = [0 for _ in range(max_num + 1)]
        self.factinv = [0 for _ in range(max_num + 1)]

        self.fact[0] = 1
        for i in range(1, max_num + 1):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod

        self.factinv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(max_num, 0, -1):
            self.factinv[i - 1] = self.factinv[i] * i
            self.factinv[i - 1] %= self.mod

    def nCk(self, n, k):
        return (self.fact[n] * self.factinv[k] * self.factinv[n - k]) % self.mod

    def nPk(self, n, k):
        return (self.fact[n] * self.factinv[n - k]) % self.mod


# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_dic = {alp[i]: i for i in range(26)}
    alp_num = [0] * 26
    for s in S:
        alp_num[alp_dic[s]] += 1
    alp_csm = [alp_num[0]]
    for an in alp_num[1:]:
        alp_csm.append(alp_csm[-1] + an)
    fc = FermatCmb(len(S), mod2)

    dp = [1] + [0] * len(S)
    for a in range(26):
        new_dp = [1] + [0] * len(S)
        for j in range(1, alp_csm[a] + 1):
            tmp = 0
            for k in range(0, min(j, alp_num[a]) + 1):
                tmp += dp[j - k] * fc.nCk(j, k)
            new_dp[j] = tmp
        dp = new_dp

    print(sum(dp[1:]) % mod2)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve(('abcdefghijklmnopqrstuvwxyz' * 5000)[:5000])
