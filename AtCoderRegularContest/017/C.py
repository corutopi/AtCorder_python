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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, W):
    if N == 1:
        print(1 if W[0] == X else 0)
        return
    w_list = W[:N // 2]
    w_dict = W[N // 2:]
    n_list = []
    n_dict = dict()
    for i in range(2 ** len(w_list)):
        # tmp = 0
        # for j in range(len(w_list)):
        #     tmp += w_list[j] if i >> j & 1 else 0
        # n_list.append(tmp)
        n_list.append(
            sum(w_list[j] if i >> j & 1 else 0 for j in range(len(w_list)))
        )
    for i in range(2 ** len(w_dict)):
        tmp = sum(w_dict[j] if i >> j & 1 else 0 for j in range(len(w_dict)))
        n_dict.setdefault(tmp, 0)
        n_dict[tmp] += 1
    print(sum(n_dict.get(X - nl, 0) for nl in n_list))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, X = map(int, input().split())
    W = [int(input()) for _ in range(N)]
    solve(N, X, W)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
