

def solve(N, As):
    As.sort()
    for i in range(1, N):
        if As[i - 1] == As[i]:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    N = int(input())
    As = [int(i) for i in input().split()]
    solve(N, As)
