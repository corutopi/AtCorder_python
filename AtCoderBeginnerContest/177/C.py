# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, As):
    mod = 10 ** 9 + 7
    tmp = sum(As)
    mlt = []
    for i in range(N):
        tmp -= As[i]
        mlt.append(tmp)
    ans = 0
    for i in range(N):
        ans += (As[i] * mlt[i]) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]

    # test
    # N = 2 * 10 ** 5
    # As = [10 ** 9 for _ in range(N)]
    solve(N, As)
