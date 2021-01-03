# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve(A, B, C, K):
    magic = 0
    while A >= B:
        B *= 2
        magic += 1
    while B >= C:
        C *= 2
        magic += 1
    print('Yes' if magic <= K else 'No')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B, C = map(int, input().split())
    K = int(input())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(A, B, C, K)
