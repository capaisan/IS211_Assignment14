def fibonacci(n):
    print(n)
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    print(f"{a}, {b}")
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])


def main():

    n = int(input("Enter a number: "))
    fibonacci(n)

    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    gcd(a,b)

    s1 = input("Enter the first word: ")
    s2 = input("Enter the second word: ")
    print(compareTo(s1, s2))



if __name__ == '__main__':
    main()
