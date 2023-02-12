def solve():
    length = [int(i) for i in input().split()]
    print(sum(length) - max(length))


if __name__ == '__main__':
    solve()
