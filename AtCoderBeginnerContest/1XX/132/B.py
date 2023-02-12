

def solve():
    n = int(input())
    P = [int(i) for i in input().split()]
    count = 0
    for i in range(1, n - 1):
        PP = [P[i - 1], P[i], P[i + 1]]
        PP.sort()
        if P[i] == PP[1] and PP[1] != PP[2]:
            count += 1
    print(count)


if __name__ == '__main__':
    solve()
