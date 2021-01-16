# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    boal = [0] * (N + 1)
    for a in A:
        boal[a] += 1
    ans = 0
    b_before = 0
    for i in range(len(boal)):
        b_num = min(K, boal[i])
        if i == 0:
            b_before = b_num
            continue
        if b_before > b_num:
            ans += i * (b_before - b_num)
            b_before = b_num
    print(ans)

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
