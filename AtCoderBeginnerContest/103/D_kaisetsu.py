# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ab):
    ab.sort(key=lambda x: x[1])
    prev = 0
    ans = 0
    for a, b in ab:
        if a + 1 <= prev:
            continue
        prev = b
        ans += 1
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ab = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, ab)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N, M = 10 ** 5, 10 ** 5
    # def tmp():
    #     a = b = randint(1, N)
    #     while a == b:
    #         b = randint(1, N)
    #     return sorted([a, b])
    # ab = [tmp() for _ in range(M)]
    # print(N, M)
    # solve(N, M, ab)
