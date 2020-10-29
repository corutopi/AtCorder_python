# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, R, S):
    S = [0 if s == '.' else 1 for s in S]
    ans = 0
    p = 0
    cnt = 0
    for i in range(1, N + 1):
        if S[N - i] == 0:
            p = max(N - i - R + 1, 0)
            cnt = 1
            break
    while p > 0:
        ans += 1
        if S[p + R - 1] == 0:
            cnt = 0
            for i in range(R):
                S[p + i] = 1
        else:
            p -= 1
            if S[p] == 0:
                cnt += 1
    if cnt > 0:
        ans += 1
    print(ans)


if __name__ == '__main__':
    N, R = map(int, input().split())
    S = input()
    solve(N, R, S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
