# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve(N, K, As):
    for i in range(N - K):
        if As[i] >= As[K + i]:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, K, As)
