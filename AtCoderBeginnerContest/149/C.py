# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from decorator import stop_watch
#
#
# @stop_watch
def solve(X):
    primes = [2]
    ans = 2
    i = 1
    while True:
        i = i + 1
        if primes[-1] >= X:
            ans = primes[-1]
            break
        flg = True
        for p in primes:
            if p > i ** 0.5:
                break
            if i % p == 0:
                flg = False
                break
        if flg:
            primes.append(i)

    print(ans)


if __name__ == '__main__':
    X = int(input())
    solve(X)
