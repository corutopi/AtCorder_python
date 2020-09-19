# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    ans = 0
    for a in range(1, N):
        b = N // a
        if N % a == 0: b -= 1
        ans += b
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
