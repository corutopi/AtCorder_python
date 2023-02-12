"""
B +/- A
"""


def solve():
    A, B = [int(i) for i in input().split()]
    result = 0
    if B % A == 0:
        result = B + A
    else:
        result = B - A
    print(result)


if __name__ == '__main__':
    solve()
