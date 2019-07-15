def solve():
    r, D, x2000 = map(int, input().split())

    xh = x2000
    for i in range(10):
        xi = r * xh - D
        print(xi)
        xh = xi


if __name__ == '__main__':
    solve()
