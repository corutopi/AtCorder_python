# import sys
# sys.setrecursionlimit(10 ** 7)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    ans = 0
    a_num = 0
    i = 0
    while i < len(S) - 1:
        if S[i] == 'A':
            a_num += 1
            i += 1
        elif S[i:i + 2] == 'BC':
            ans += a_num
            i += 2
        else:
            a_num = 0
            i += 1
    print(ans)

if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve(random_str(200000, 'ABC'))
    # solve('ABC' * (200000 // 3))
