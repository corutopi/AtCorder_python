# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(1, S // 3 + 1):
        tama = i + (S - (i * 3))
        tama -= 2
        bo = i - 1
        ans += cmb(tama + 1, bo)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    # S = input()
    S = int(input())
    # N, M = map(int, input().split())
    # Ai = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(S)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
