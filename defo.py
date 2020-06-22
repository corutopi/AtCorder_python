# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve():
    S = 'aaa'
    for s in list(S):
        if S.count(s) != 2:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve()
