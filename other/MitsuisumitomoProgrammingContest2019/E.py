# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    dp = [0] * N
    ans = 1
    for i in range(N):
        if A[i] == 0:
            ans *= 3 - dp[A[i]]
        else:
            ans *= dp[A[i] - 1] - dp[A[i]]
        dp[A[i]] += 1
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
