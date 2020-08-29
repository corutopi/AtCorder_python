# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S, T):
    ans = 10000
    for i in range(len(S) - len(T) + 1):
        tmp = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                tmp += 1
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    S = input()
    T = input()
    # N = int(input())
    # N, M = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(S, T)
