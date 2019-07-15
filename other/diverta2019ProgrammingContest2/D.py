
def solve():
    N = int(input())
    gA, sA, bA = map(int, input().split())
    gB, sB, bB = map(int, input().split())
    values = [[gA, gB], [sA, sB], [bA, bB]]
    print(values)

    # A -> B
    values.sort(key=lambda x: x[1] - x[0], reverse=True)
    metals = [0, 0, 0]
    # # exchange on A, dongri to metal
    for i in range(len(values)):
        if values[i][1] - values[i][0] <= 0:
            break
        A = values[i][0]
        while N > A:
            metals[i] += 1
            N -= A
    # # exchange on B, metal to dongri
    for i in range(len(values)):
        B = values[i][1]
        N += metals[i] * B
        metals[i] = 0

    # B -> A
    values.sort(key=lambda x: x[0] - x[1], reverse=True)
    metals = [0, 0, 0]
    # # exchange on B, dongri to metal
    for i in range(len(values)):
        if values[i][0] - values[i][1] <= 0:
            break
        B = values[i][1]
        while N > B:
            metals[i] += 1
            N -= B
    # # exchange on A, metal to dongri
    for i in range(len(values)):
        A = values[i][0]
        N += metals[i] * A
        metals[i] = 0
    print(N)




if __name__ == '__main__':
    solve()
