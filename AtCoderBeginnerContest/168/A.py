

def solve():
    N = int(input()[-1])
    if N in [2,4,5,7,9]:
        print('hon')
    elif N in [0,1,6,8]:
        print('pon')
    elif N in [3]:
        print('bon')


if __name__ == '__main__':
    solve()
