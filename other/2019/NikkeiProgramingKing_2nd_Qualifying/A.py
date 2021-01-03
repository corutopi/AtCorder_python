

def solve():
    N = int(input())
    if N % 2 == 1:
        print((N - 1) // 2)
    else:
        print((N - 2) // 2)


if __name__ == '__main__':
    solve()
