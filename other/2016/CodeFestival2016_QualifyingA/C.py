# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import string
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(s, K):
    alp = {string.ascii_lowercase[i]: i for i in range(26)}
    ans = [alp[ss] for ss in s]
    n = 0
    for i in range(len(ans)):
        if ans[i] == 0:
            continue
        if K - n >= 26 - ans[i]:
            n += 26 - ans[i]
            ans[i] = 0
        if K - n == 0:
            break
    if K - n != 0:
        ans[-1] = (((K - n) % 26) + ans[-1]) % 26
    print(''.join([string.ascii_lowercase[a] for a in ans]))


if __name__ == '__main__':
    s = input()
    K = int(input())
    solve(s, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # s = random_str(10 ** 5, string.ascii_lowercase)
    # K = randint(1, 10 ** 9)
    # solve(s, K)
