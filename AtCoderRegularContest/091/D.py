# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K):
    ans = 0
    for i in range(1, N + 1):
        ans += N // i * max(0, i - K)
        ans += max(0, N % i - K + 1) if K != 0 else N % i
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
