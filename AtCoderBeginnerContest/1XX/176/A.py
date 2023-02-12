# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, T):
    ans = N // X * T
    if N % X > 0:
        ans += T
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, X, T = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, X, T)
