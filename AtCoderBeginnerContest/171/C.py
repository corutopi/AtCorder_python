# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    number27 = []
    cnt = 26
    digit = 1
    while N > 0:
        if N <= cnt:
            break
        else:
            N -= cnt
            cnt *= 26
            digit += 1
    ans = list('a' * digit)
    N -= 1
    tmp = -1
    while N > 0:
        N, mod = divmod(N, 26)
        ans[tmp] = alp[mod]
        tmp -= 1
    print(''.join(ans))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N)
    # for i in range(1, 100):
    #     # print(i)
    #     solve(i)
