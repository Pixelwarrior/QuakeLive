import os
import random
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def save_stats(correct, incorrect):
    with open("stats.txt", "w") as file:
        file.write(f"{correct}\n")
        file.write(f"{incorrect}\n")

def load_stats():
    try:
        with open("stats.txt", "r") as file:
            lines = file.readlines()
            correct_count = int(lines[0].strip())
            incorrect_count = int(lines[1].strip())
        return correct_count, incorrect_count
    except FileNotFoundError:
        return 0, 0


def main():
    print("Quake Live Duel timings")
    correct_count, incorrect_count = load_stats()
    print("=== Previous Stats ===")
    print("Total Correct Answers: ", correct_count)
    print("Total Incorrect Answers: ", incorrect_count)
    input_value = input("[1] : Red | [2] : Mega - ")
    if input_value not in ["1", "2"]:
        print("Invalid input. Please select 1 or 2.")
        return

    correct_count = 0
    incorrect_count = 0
    game_mode = int(input_value)

    while True:
        random_number = random.randint(0, 59)
        print(random_number)
        input_value2 = input("")
        
        if input_value2.lower() == "exit":
            print("\n=== Stats ===\n")
            print("Correct answers:", correct_count)
            print("Incorrect answers:", incorrect_count)
            save_stats(correct_count, incorrect_count)
            break

        try:
            user_answer = int(input_value2)
            if game_mode == 1:
                correct_answer = (random_number + 25) % 60
            else:
                correct_answer = (random_number + 35) % 60

            if user_answer == correct_answer:
                print("Correct!")
                correct_count += 1
            else:
                print("Incorrect. The correct answer was:", correct_answer)
                incorrect_count += 1

            if (correct_count + incorrect_count) % 5 == 0:
                clear_screen()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    main()
