def fibonacci_sequence(N):
    fibo = [0,1]
    print(len(fibo))
    
    while N != 0:
        size = len(fibo)
        num = fibo[(size-1)] + fibo[(size-2)]
        fibo.append(num)
        print(fibo)
        N = N-1

    return fibo

def main():
    index = input('Digite N:')
    fibonacci_sequence(int(index))

main()

