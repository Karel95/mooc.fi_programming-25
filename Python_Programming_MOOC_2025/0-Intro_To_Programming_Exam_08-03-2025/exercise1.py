# Write your solution to exercise 1 here

def main():
    numbers = []

    while True:
        num = int(input("Type in a number: "))
        if num == 0:
            break
        numbers.append(num)

    if numbers:
        smallest = min(numbers)
        biggest = max(numbers)
        amount = len(numbers)
        total_sum = sum(numbers)
        most_repeated = max(set(numbers), key=numbers.count)

        print(f"Biggest: {biggest}")
        print(f"Smallest: {smallest}")
        print(f"Number of numbers: {amount}")
        print(f"Sum: {total_sum}")
        print(f"Most repeated: {most_repeated}")

if __name__ == "__main__":
    main()
