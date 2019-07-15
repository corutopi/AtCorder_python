
def solve():
    a = int(input())
    a += sum([int(i) for i in input().split()])
    print(a, input())
    pass


if __name__ == '__main__':
    solve()
