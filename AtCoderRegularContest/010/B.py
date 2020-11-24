# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, md):
    days = [1 if i % 7 in [1, 0] else 0 for i in range(366 + 1)]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_cs = [0, 0]
    for m in months:
        months_cs.append(months_cs[-1] + m)

    dd = []
    for mmdd in md:
        m, d = mmdd.split('/')
        dd.append(months_cs[int(m)] + int(d))
    dd.sort()

    for d in dd:
        while True:
            if days[d] == 0:
                days[d] = 1
                break
            d += 1
            if d > 366:
                break

    ans = 0
    tmp = 0
    for d in days[1:] + [0]:
        if d == 1:
            tmp += 1
        if d == 0:
            ans = max(ans, tmp)
            tmp = 0

    print(ans)


if __name__ == '__main__':
    N = int(input())
    md = [input() for _ in range(N)]
    solve(N, md)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
