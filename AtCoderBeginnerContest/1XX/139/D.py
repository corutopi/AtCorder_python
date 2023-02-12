# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    n = N - 1
    print((n + 1) * n // 2)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N)
