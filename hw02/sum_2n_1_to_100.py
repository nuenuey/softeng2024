from hw02.odd_h_j import is_even


def main():
    total=0

    for i in range(1,101):
        # total = total+i
        if is_even(i):
             total += i
    print(f"1부터 100까지의 짝수 합은 {total}입니다")

if __name__ == "__main__":
    main()