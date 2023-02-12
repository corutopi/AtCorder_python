# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B, C, X, Y):
    ans = A * X + B * Y
    x = X
    y = Y
    while x + y != 0:
        if x <= 0 or y <= 0:
            pass
        ans = min(ans, ans - A * min(1, x) - B * min(1, y) + C * 2)
        x = max(0, x - 1)
        y = max(0, y - 1)
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B, C, X, Y = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(A, B, C, X, Y)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
