import functools


def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    L = []
    R = []
    for i in range(N):
        pass
    max_gcd = 1
    for i in range(N):
        A_ = A.copy()
        A_.remove(A[i])
        max_gcd = max(max_gcd, functools.reduce(gcd, A_))
    print(max_gcd)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    solve()
