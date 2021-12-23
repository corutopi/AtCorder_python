import sys
sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    digit_mod = [1]
    for _ in range(len(S)):
        digit_mod.append((digit_mod[-1] * 3) % mod)
    ans = 0

    def xxx(i):
        if i == len(S):
            return 1
        tmp = 0
        if S[i] == '1':
            # a + b の現在の桁が0の場合のパターン:
            #   現在の桁以外が[0,0], [0,1], [1,0] になればよいので 3 ** x
            tmp += digit_mod[len(S) - (i + 1)]
            # a + b の現在の桁が1の場合のパターン:
            #   現在の桁以降に1が存在する場合, その1以降のみの数で作れるパターン * 2
            #   存在しない場合, 1([0,0] のパターンのみ) * 2
            tmp += xxx(i + 1) * 2
        else:
            tmp += xxx(i + 1)
        return tmp

    print(xxx(0) % mod)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve('1' * 100001)
