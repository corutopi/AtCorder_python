

def solve():
    N = int(input())
    for i in range(1, 10):
        q, mod = divmod(N, i)
        if q <= 9 and mod == 0:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    solve()
