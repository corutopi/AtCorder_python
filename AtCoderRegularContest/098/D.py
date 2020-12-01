# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    xor_cs = [0]
    sum_cs = [0]
    for a in A:
        xor_cs.append(xor_cs[-1] ^ a)
        sum_cs.append(sum_cs[-1] + a)
    l, r = 1, 1
    ans = 0
    while l <= N:
        if r < N:
            xor_lr = xor_cs[r + 1] ^ xor_cs[l - 1]
            sum_lr = sum_cs[r + 1] - sum_cs[l - 1]
            if xor_lr == sum_lr:
                r += 1
            else:
                ans += r - l + 1
                l += 1
        else:
            ans += r - l + 1
            l += 1
        if l > r:
            r += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
