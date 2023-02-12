# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    S = 'aaa'
    x = 0
    for n in N:
        x += int(n)
    print('Yes' if x % 9 == 0 else 'No')


if __name__ == '__main__':
    # S = input()
    N = input()
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N)
