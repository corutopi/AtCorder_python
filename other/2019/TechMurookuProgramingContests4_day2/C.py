
def solve():
    A, B = map(int, input().split())
    if A == 0:
        if B % 2 == 1:
            print('Angel')
        else:
            print('Devil')
    elif B == 0:
        print('Devil')
    elif A % 2 == 1 and B % 2 == 1:
        print('Angel')
    else:
        print('Devil')


if __name__ == '__main__':
    solve()
