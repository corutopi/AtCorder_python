"""
B - Digital Gifts
"""


def solve():
    N = int(input())
    sum_ochotama = 0
    for n in range(N):
        x, u = input().split()
        x = float(x)
        sum_ochotama += x if u == 'JPY' else x * 380000
    print(sum_ochotama)


if __name__ == '__main__':
    solve()
