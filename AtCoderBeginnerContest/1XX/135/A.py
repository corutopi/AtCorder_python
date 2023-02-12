

def solve():
    A, B = map(int, input().split())
    K2 = A + B
    if K2 % 2 == 0:
        print(K2 // 2)
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    solve()
