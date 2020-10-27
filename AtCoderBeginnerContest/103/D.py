# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ab):
    l = [[] for _ in range(N + 1)]
    r = [[] for _ in range(N + 1)]
    ab_flg = [0] * M
    for i in range(M):
        l[ab[i][0]].append(i)
        r[ab[i][1]].append(i)

    dq = deque([])
    ans = 0
    for i in range(1, N + 1):
        for ri in r[i]:
            if ab_flg[ri] == 0:
                ans += 1
                while dq:
                    ab_flg[dq.pop()] = 1
                break
        for li in l[i]:
            dq.append(li)

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
