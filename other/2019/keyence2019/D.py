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
def solve(N, M, A, B):
    fc = FermatCmb(N * M, mod)
    COLUMN, ROW = 1, 0

    AB = [[a, ROW] for a in A] + [[b, COLUMN] for b in B]
    AB.sort()

    if len(A) != len(set(A)) or len(B) != len(set(B)):
        print(0)
        return

    ans = 1
    draw_cnt = 0
    row_cnt = 0
    cln_cnt = 0
    for i in range(len(AB)):
        x, rc = AB[i]
        if rc == ROW and i < len(AB) - 1 and x == AB[i + 1][0]:
            continue
        if rc == COLUMN and i > 0 and x == AB[i - 1][0]:
            if x - draw_cnt < N + M - 1 - row_cnt - cln_cnt:
                ans = 0
                break
            ans *= fc.nPk(x - draw_cnt - 1, N + M - 1 - row_cnt - cln_cnt - 1)
            draw_cnt += N + M - 1 - row_cnt - cln_cnt
            row_cnt += 1
            cln_cnt += 1
        else:
            t = M if rc == ROW else N
            c = cln_cnt if rc == ROW else row_cnt
            if x - draw_cnt < t - c:
                ans = 0
                break
            ans *= (t - c) * fc.nPk(x - draw_cnt - 1, t - c - 1)
            draw_cnt += t - c
            if rc == ROW:
                row_cnt += 1
            else:
                cln_cnt += 1
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, M, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
