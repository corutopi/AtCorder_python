def solve():
    L, R = map(int, input().split())
    if L + 2019 <= R:
        print(0)
    elif L % 2019 > R % 2019:
        print(0)
    else:
        l = L % 2019
        r = R % 2019
        min_mod = 2019
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                min_mod = min(min_mod, (i * j) % 2019)
        print(min_mod)


if __name__ == '__main__':
    solve()
