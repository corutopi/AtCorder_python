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
def solve(N, T, A):
    T = [0] + T + [0]
    A = [0] + A + [0]
    ans = 1
    for i in range(1, N + 1):
        if T[i - 1] != T[i] and A[i + 1] != A[i] and T[i] != A[i]:
            # A,T両方更新されたのにそれぞれの値が異なる
            ans = 0
            break
        if T[i - 1] != T[i] and T[i] > A[i]:
            # Tの記録が更新されたのにAのほうが小さい
            ans = 0
            break
        if A[i + 1] != A[i] and A[i] > T[i]:
            # Aの記録が更新されたのにTのほうが小さい
            ans = 0
            break

        if T[i - 1] != T[i] or A[i + 1] != A[i]:
            # どちらかの値が更新されていればhiは一意に決まる
            continue

        ans *= min(T[i], A[i])
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N = int(input())
    T = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    solve(N, T, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
