import math


def solve():
    count = 0
    R, G, B, N = map(int, input().split())
    # print(math.floor(N / R))
    for r in range(math.floor(N / R) + 1):
        # print('G購入上限:', math.floor(((N - (R * r)) / G)))
        for g in range(math.floor(((N - (R * r)) / G)) + 1):
            if (N - (R * r) - (G * g)) % B == 0:
                # print('残数:', N - (R * r) - (G * g))
                # print(r, g, (N - (R * r) - (G * g)) / B)
                count += 1
    print(count)


if __name__ == '__main__':
    solve()
