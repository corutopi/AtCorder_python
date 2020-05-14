

def solve():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    isMulti = 1 if x == W / 2 and y == H / 2 else 0
    print(area, isMulti)


if __name__ == '__main__':
    solve()
