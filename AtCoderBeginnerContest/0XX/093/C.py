# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B, C):
    ans = 0
    while A != B or A != C:
        A, B, C = sorted([A, B, C])
        if abs(A - B) >= 1:
            A += 2
        else:
            A += 1
            B += 1
        ans += 1
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B, C = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(A, B, C)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
