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
def solve(S, K):
    # X . の連続数をそれぞれ配列にする
    X = []
    dot = [] if S[0] == '.' else [0]
    before = 'a'
    i = 0
    for s in S + 'a':
        if s != before:
            if before == 'a':
                pass
            elif before == 'X':
                X.append(i)
            elif before == '.':
                dot.append(i)
            before = s
            i = 0
        i += 1
    if sum(dot) <= K:
        print(len(S))
        return
    if sum(X) == 0:
        print(min(len(S), K))
        return
    dot += [] if S[-1] == '.' else [0]
    # X の累積和を作る
    cs_X = [0]
    for x in X:
        cs_X.append(cs_X[-1] + x)
    # . で尺取り法をする
    ans = 0
    head = 1
    tail = 0
    shaku = 0
    while head < len(dot):
        while shaku <= K and head < len(dot):
            ans = max(ans, K + cs_X[min(head, len(dot) - 1)] - cs_X[tail])
            shaku += dot[head]
            head += 1
        while shaku > K:
            shaku -= dot[tail + 1]
            tail += 1

    print(ans)


if __name__ == '__main__':
    S = input()
    K = int(input())
    solve(S, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
