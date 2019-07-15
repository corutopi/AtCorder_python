def solve():
    A, B = map(int, input().split())

    if A <= 5:
        price = 0
    elif 6 <= A <= 12:
        price = int(B / 2)
    else:
        price = B

    print(price)


if __name__ == '__main__':
    solve()
