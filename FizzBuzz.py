while True:
    try:
        num_elements = int(input("Enter the number of elements for FizzBuzz: "))

        num_fizz = 0
        num_buzz = 0
        num_fizz_buzz = 0

        print("\n--- FizzBuzz Sequence ---")

        for i in range(1, num_elements + 1):
            print(f"Iteration {i}:", end=" ")

            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
                num_fizz_buzz += 1

            elif i % 3 == 0:
                print("Fizz")
                num_fizz += 1

            elif i % 5 == 0:
                print("Buzz")
                num_buzz += 1

            else:
                print(i)

        print("\n--- Summary ---")
        print(f"Total Fizz: {num_fizz}")
        print(f"Total Buzz: {num_buzz}")
        print(f"Total FizzBuzz: {num_fizz_buzz}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    choice = input("\nWould you like to exit the program? (yes/no): ").strip().lower()
    if choice in ['yes', 'y']:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("\nRestarting program...\n")