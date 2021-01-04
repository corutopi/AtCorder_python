# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(s):
    mark = ['S', 'H', 'D', 'C']
    need_num = ['A', '10', 'J', 'Q', 'K']
    for m in mark:
        s = s.replace(m, ' ' + m)
    s = s.strip()
    decki = s.split()
    decki = [[d[0], d[1:]] for d in decki]

    ans = [0] * 100  # more than trump card
    for m in mark:
        tmp = []
        all_count = 0
        need_count = 0
        for card in decki:
            all_count += 1
            if (card[0] != m) or (card[0] == m and card[1] not in need_num):
                tmp.append(card)
            else:
                need_count += 1
            if need_count == 5:
                break
        ans = ans if len(ans) < len(tmp) else tmp

    if len(ans) == 0:
        print(0)
    else:
        print(''.join([''.join(a) for a in ans]))


if __name__ == '__main__':
    s = input()
    solve(s)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
