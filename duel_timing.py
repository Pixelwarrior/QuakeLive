import os, random, platform

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def save_stats(correct, incorrect):
    with open("stats.txt", "w") as file:
        file.write(f"{correct}\n{incorrect}\n")

def load_stats():
    try:
        with open("stats.txt", "r") as file:
            correct, incorrect = map(int, file.readlines())
        return correct, incorrect
    except FileNotFoundError:
        return 0, 0

def main():
    print("Quake Live Duel timings")
    correct, incorrect = load_stats()
    print("=== Previous Stats ===")
    print("Total Correct Answers:", correct)
    print("Total Incorrect Answers:", incorrect)
    mode = int(input("[1] : Red | [2] : Mega - "))
    if mode not in [1, 2]:
        print("Invalid input. Please select 1 or 2.")
        return

    correct, incorrect = 0, 0

    while True:
        random_number = random.randint(0, 59)
        print(random_number)
        user_input = input("")
        
        if user_input.lower() == "exit":
            print("\n=== Stats ===\n")
            print("Correct answers:", correct)
            print("Incorrect answers:", incorrect)
            save_stats(correct, incorrect)
            break

        try:
            user_answer = int(user_input)
            correct_answer = (random_number + 25 if mode == 1 else random_number + 35) % 60

            if user_answer == correct_answer:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect. The correct answer was:", correct_answer)
                incorrect += 1

            if (correct + incorrect) % 5 == 0:
                clear_screen()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
