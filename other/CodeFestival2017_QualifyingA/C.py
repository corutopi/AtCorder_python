# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, a):
    alps = {}
    for ah in a:
        for ahw in ah:
            alps.setdefault(ahw, 0)
            alps[ahw] += 1
    lim_2not4 = 0
    lim_odd = 0
    if H % 2 == 1 and W % 2 == 1:
        lim_2not4 = (H - 1) // 2 + (W - 1) // 2
        lim_odd = 1
    elif H % 2 == 1:
        lim_2not4 = W // 2
    elif W % 2 == 1:
        lim_2not4 = H // 2

    num_2not4 = 0
    num_odd = 0
    for alp in alps.values():
        if alp % 4 == 0:
            pass
        elif alp % 2 == 0:
            num_2not4 += 1
        else:
            num_odd += 1
        if num_2not4 > lim_2not4 or num_odd > lim_odd:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    solve(H, W, a)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
