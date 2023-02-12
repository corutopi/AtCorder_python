# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def lcm(a, b):
    """最小公倍数"""
    from math import gcd
    return (a * b) // gcd(a, b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B, C, D):
    A -= 1
    non_div_A = A - (A // C) - (A // D) + (A // lcm(C, D))
    non_div_B = B - (B // C) - (B // D) + (B // lcm(C, D))
    print(non_div_B - non_div_A)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B, C, D = map(int, input().split())
    # As = [int(i) for i in input().split()]
    # Bs = [int(i) for i in input().split()]
    solve(A, B, C, D)
