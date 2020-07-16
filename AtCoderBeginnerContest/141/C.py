# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, Q, As):
    rev_point = [0] * (N + 1)
    for A in As:
        rev_point[A] += 1
    for rp in rev_point[1:]:
        if K - (Q - rp) > 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K, Q = map(int, input().split())
    As = [int(input()) for _ in range(Q)]
    # Bs = [int(i) for i in input().split()]
    solve(N, K, Q, As)
