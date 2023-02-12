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
def solve(S):
    a_after = 0
    while S[-(a_after + 1)] == 'a':
        a_after += 1
        if a_after == len(S):
            # print('Yes')
            return 'Yes'

    a_before = 0
    while S[a_before] == 'a':
        a_before += 1
    if a_before > a_after:
        return 'No'

    s = 'a' * (a_after - a_before) + S

    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            # print('No')
            # break
            return 'No'
    else:
        # print('Yes')
        return 'Yes'


def real_solve(S):
    for i in range(0, 11):
        s = 'a' * i + S
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                break
        else:
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    S = input()
    print(solve(S))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     S = random_str(randint(1, 10), 'abcd')
    #     if solve(S) != real_solve(S):
    #         print(S)
    #         break