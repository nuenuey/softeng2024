def is_prime(n : int) -> bool:
    if n <2:
        return False

    for i in range(2, n):
        if n% 1 ==0:
            return False

    return True

def main():
    n = 7

if __name__ == '__main__':
    main()