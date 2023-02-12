# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(s, x, y):
    split_s = s.split('T')
    to_x = [len(split_s[i]) for i in range(len(split_s)) if i % 2 == 0]
    to_y = [len(split_s[i]) for i in range(len(split_s)) if i % 2 == 1]

    dict_x = {to_x[0]: 1}
    max_x = sum(to_x)
    for tx in to_x[1:]:
        if tx == 0: continue
        new_dict_x = {}
        for mx in range(-max_x, max_x + 1):
            if dict_x.get(mx, -1) == 1:
                new_dict_x[mx + tx] = 1
                new_dict_x[mx - tx] = 1
        dict_x = new_dict_x
    if dict_x.get(x, -1) == -1:
        print('No')
        return

    dict_y = {0: 1}
    max_y = sum(to_y)
    for ty in to_y:
        if ty == 0: continue
        new_dict_y = {}
        for my in range(-max_y, max_y + 1):
            if dict_y.get(my, -1) == 1:
                new_dict_y[my + ty] = 1
                new_dict_y[my - ty] = 1
        dict_y = new_dict_y
    if dict_y.get(y, -1) == -1:
        print('No')
        return

    print('Yes')


if __name__ == '__main__':
    s = input()
    x, y = map(int, input().split())
    solve(s, x, y)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # while True:
    #     s = random_str(10, 'TF')
    #     x, y = randint(1, len(s) // 2), randint(1, len(s) // 2)
    #     solve(s, x, y)
