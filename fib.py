import math

def fib(n):
    cinco_raiz = math.sqrt(5)
    num = (cinco_raiz/5)*((((1+cinco_raiz)/2)**n)-((1-cinco_raiz)/2)**n)
    return num

def main():
    for i in range(20):
        print(fib(i))

if __name__ == "__main__":
    main()
