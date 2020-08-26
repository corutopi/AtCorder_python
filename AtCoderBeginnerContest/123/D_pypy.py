# 解説を参考に作成

# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y, Z, K, As, Bs, Cs):
    ABs = []
    for A in As:
        for B in Bs:
            ABs.append(A + B)
    ABs.sort(reverse=True)
    ABCs = []
    for i in range(min(X * Y, K)):
        AB = ABs[i]
        for C in Cs:
            ABCs.append(AB + C)
    ABCs.sort(reverse=True)
    for i in range(K):
        print(ABCs[i])


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    X, Y, Z, K = map(int, input().split())
    As = [int(i) for i in input().split()]
    Bs = [int(i) for i in input().split()]
    Cs = [int(i) for i in input().split()]
    # import random
    # X, Y, Z, K = 1000,1000,1000,3000
    # As = [random.randint(1, 10 ** 10) for _ in range(X)]
    # Bs = [random.randint(1, 10 ** 10) for _ in range(Y)]
    # Cs = [random.randint(1, 10 ** 10) for _ in range(Z)]
    solve(X, Y, Z, K, As, Bs, Cs)
