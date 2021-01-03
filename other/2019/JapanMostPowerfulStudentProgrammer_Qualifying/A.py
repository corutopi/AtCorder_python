

def solve():
    M, D = map(int, input().split())
    count = 0
    for d in range(1, D + 1):
        d1 = d % 10
        d10 = int(d / 10)
        if d1 >= 2 and d10 >= 2 and 0 < d1 * d10 <= M:
            count += 1
    print(count)


if __name__ == '__main__':
    solve()
