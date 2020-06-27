# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re





from decorator import stop_watch


@stop_watch
def solve(N):
    pf = [{}, {}]
    def prime_factorization(x, readOnly=False):
        """素因数分解"""
        re = dict()
        i = 2
        while x != 1:
            if x % i == 0:
                if x // i == 1:
                    # 素数の場合
                    re.setdefault(i, 0)
                    re[i] += 1
                    x //= i
                else:
                    re = pf[x // i].copy()
                    re.setdefault(i, 0)
                    re[i] += 1
                    break
            else:
                i += 1
        if not readOnly:
            pf.append(re)
        return re

    ans = 0
    for i in range(1, N + 1):
        if i == 1:
            ans += 1
        else:
            sub = i
            # print(i, prime_factorization(i, True))
            for k, v in prime_factorization(i).items():
                sub *= (v + 1)
            ans += sub

    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)
    # print(prime_factorization(10000000))
    pass
