import math


def solve():
    A, B, H, M = map(int, input().split())
    Aa = H * (360 / 12) + M * (30 / 60)
    Ba = M * (360 / 60)
    a = abs(Aa - Ba)
    a = min(a, 360 - a)

    if a == 0:
        print(abs(A - B))
    elif a == 180:
        print(A + B)
    else:
        print(
            math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(a))))


if __name__ == '__main__':
    solve()
