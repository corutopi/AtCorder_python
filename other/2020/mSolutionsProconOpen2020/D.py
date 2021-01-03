# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from decorator import stop_watch


@stop_watch
def solve(N, As):
    money = 1000
    stock = 0
    for i in range(len(As)):
        if i == N - 1:
            money += stock * As[i]
            stock = 0
            continue
        if As[i] > As[i + 1]:
            money += stock * As[i]
            stock = 0
        if As[i] < As[i + 1]:
            stock += money // As[i]
            money = money % As[i]
    print(money)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(N, As)
