# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    ADD_COMBO, RETURN_KABURIN = 0, 1
    charge = 0
    combo = 0
    damage = 0
    kaburin_num = 5
    hq = []
    for t in range(len(S)):
        s = S[t]
        charge -= 1
        while hq:
            if hq[0][0] > t: break
            _, action = heappop(hq)
            if action == ADD_COMBO:
                combo += 1
            elif action == RETURN_KABURIN:
                kaburin_num += 1
        if charge > 0: continue
        if s == '-':
            pass
        elif s == 'N':
            if kaburin_num < 1: continue
            charge = 0.5
            damage += int(10 * (10 + combo // 10)) // 10
            heappush(hq, [t + 0.5 + 1, ADD_COMBO])
            kaburin_num -= 1
            heappush(hq, [t + 0.5 + 1 + 5, RETURN_KABURIN])
        elif s == 'C':
            if kaburin_num < 3: continue
            charge = 2.5
            damage += int(50 * (10 + combo // 10)) // 10
            heappush(hq, [t + 2.5 + 1, ADD_COMBO])
            kaburin_num -= 3
            heappush(hq, [t + 2.5 + 1 + 5, RETURN_KABURIN])
            heappush(hq, [t + 2.5 + 1 + 5, RETURN_KABURIN])
            heappush(hq, [t + 2.5 + 1 + 5, RETURN_KABURIN])
    print(damage)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve(random_str(10 ** 6, 'N'))
    # solve(random_str(10 ** 6, 'C'))
    # solve(('NNC-----' * 10 ** 6)[:10 ** 6])
