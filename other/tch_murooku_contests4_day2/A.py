

def solve():
    x, y = map(int, input().split())
    if y % 2 == 0 and y // 2 >= abs(x) and (y // 2 - x) % 2 == 0:
        print(y // 2)
    else:
        print(-1)


if __name__ == '__main__':
    solve()
