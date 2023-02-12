# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, xy):
    ans = 0
    frend_map = [[] for _ in range(N + 1)]
    for x, y in xy:
        frend_map[x].append(y)
        frend_map[y].append(x)

    for i in range(2 ** N):
        menber = []
        for j in range(N):
            if i >> j & 1:
                menber.append(j + 1)
        flg = True
        for m in range(len(menber)):
            mm = menber[m]
            for n in menber[m + 1:]:
                if not n in frend_map[mm]:
                    flg = False
                    break
            if not flg:
                break
        if flg:
            ans = max(ans, len(menber))
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    xy = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, xy)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
