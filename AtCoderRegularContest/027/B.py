# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, S1, S2):
    for i in range(N):
        if S1[i].isalpha() and S2[i].isalpha() and S1[i] != S2[i]:
            S1 = S1.replace(S2[i], S1[i])
            S2 = S2.replace(S2[i], S1[i])
    for i in range(N):
        if S1[i].isalpha() and S2[i].isalpha() and S1[i] != S2[i]:
            S2 = S2.replace(S1[i], S2[i])
            S1 = S1.replace(S1[i], S2[i])
    for _ in range(18):
        for i in range(N):
            if S1[i].isalpha() and S2[i].isdigit():
                alp = S1[i]
                digit = S2[i]
                S1 = S1.replace(alp, digit)
                S2 = S2.replace(alp, digit)
        for i in range(N):
            if S1[i].isdigit() and S2[i].isalpha():
                alp = S2[i]
                digit = S1[i]
                S1 = S1.replace(alp, digit)
                S2 = S2.replace(alp, digit)
    ans = 1
    readed = []
    for i in range(N):
        if S1[i] in readed:
            continue
        if S1[i].isalpha():
            if i == 0:
                ans *= 9
            else:
                ans *= 10
            readed.append(S1[i])
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    S1 = input()
    S2 = input()
    solve(N, S1, S2)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
