# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(2,10):
        fibs.append(fibs[i - 1] + fibs[i - 2])

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
