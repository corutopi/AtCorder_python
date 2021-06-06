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
def solve(N, K, S):
    ans = [s for s in S[N - K:]]
    remove_point = 0
    while remove_point < K - 1 and ans[remove_point] <= ans[remove_point + 1]:
        remove_point += 1
    for s in reversed(S[:N - K]):
        if s <= ans[0]:
            ans.pop(remove_point)
            ans = [s] + ans
            while remove_point < K - 1 and \
                    ans[remove_point] <= ans[remove_point + 1]:
                remove_point += 1
    print(''.join(ans))


if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()
    solve(N, K, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10 ** 5
    # K = 50000
    # S = random_str(N, string.ascii_lowercase)
    # solve(N, K, S)
