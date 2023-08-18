def printer(x):
    for i in range(x):
        print(i)

if __name__ == '__main__':
    print("How high to go?")
    x = int(input())
    printer(x)