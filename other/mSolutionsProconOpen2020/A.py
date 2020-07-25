# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve(X):
    ans = 1
    if X <= 1999:
        ans = 1
    if X <= 1799:
        ans = 2
    if X <= 1599:
        ans = 3
    if X <= 1399:
        ans = 4
    if X <= 1199:
        ans = 5
    if X <= 999:
        ans = 6
    if X <= 799:
        ans = 7
    if X <= 599:
        ans = 8
    print(ans)


if __name__ == '__main__':
    # S = input()
    X = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(X)
