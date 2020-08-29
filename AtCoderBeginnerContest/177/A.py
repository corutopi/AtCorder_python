# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(D, T, S):
    if S * T >= D:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    D, T, S = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(D, T, S)
