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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    x = min(N, 8)
    cmb = [[] for _ in range(200)]
    for i in range(1, 2 ** x):
        tmp = []
        tmp_sum = 0
        for j in range(x):
            if i >> j & 1:
                tmp.append(j + 1)
                tmp_sum += A[j]
        cmb[tmp_sum % 200].append(tmp)
    for c in cmb:
        if len(c) >= 2:
            print('Yes')
            print(len(c[0]), ' '.join([str(s) for s in c[0]]))
            print(len(c[1]), ' '.join([str(s) for s in c[1]]))
            return
    print('No')


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
