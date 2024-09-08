def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



def main():
    n = int(input("숫자를 입력하시오 ===>"))
    print(f"{n}의 팩토리얼은 {n * factorial(n-1) }입니다.")

if __name__ == '__main__':
    main()