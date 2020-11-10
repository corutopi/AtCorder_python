# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    from math import gcd
    g = max(A)
    if g < K:
        print('IMPOSSIBLE')
        return
    for a in A:
        g = gcd(g, a)
    if K % g == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
