# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, As):
    import math
    primes = [0] * (max(As) + 1)
    pairwise_flg = True
    for x in As:
        i = 2
        while x != 1:
            if x % i == 0:
                if primes[i] != 0:
                    pairwise_flg = False
                    break
                primes[i] = 1
                while x % i == 0:
                    x = x // i
            else:
                i += 1
                if i > math.sqrt(x):
                    if primes[x] != 0:
                        pairwise_flg = False
                    else:
                        primes[x] = 1
                    break
        if not pairwise_flg:
            break
    if pairwise_flg:
        print('pairwise coprime')
        return

    tmp = math.gcd(As[0], As[1])
    for A in As:
        tmp = math.gcd(tmp, A)
    if tmp == 1:
        print('setwise coprime')
        return

    print('not coprime')


if __name__ == '__main__':
    N = int(input())
    As = [int(i) for i in input().split()]
    # # test
    # import random
    # N = 10 ** 6
    # As = [random.randint(1, 10 ** 6) for _ in range(N)]
    solve(N, As)

