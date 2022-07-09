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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, X):
    number_num = [0] * (10 ** 5 + 1)
    mod_num = [0] * M
    for x in X:
        number_num[x] += 1
        mod_num[x % M] += 1
    ans = 0
    for i in range(M):
        if i == 0 or (M % 2 == 0 and i == M // 2):
            if mod_num[i] > 0:
                ans += mod_num[i] // 2
                mod_num[i] = mod_num[i] % 2
        else:
            if mod_num[i] > 0 and mod_num[M - i] > 0:
                tmp = min(mod_num[i], mod_num[M - i])
                ans += tmp
                mod_num[i] -= tmp
                mod_num[M - i] -= tmp
    for i in range(len(number_num)):
        while number_num[i] >= 2 and mod_num[i % M] >= 2:
            ans += 1
            number_num[i] -= 2
            mod_num[i % M] -= 2
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = [int(i) for i in input().split()]
    solve(N, M, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
