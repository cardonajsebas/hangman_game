import random
import sys
from colorama import Fore, Style, init
from pics import HANGMAN_PICS, TITLE


init(autoreset=True)


DIFFICULTIES = {"1": "Easy", "2": "Medium", "3": "Hard"}
LIVES_BY_DIFFICULTY = {"1": 10, "2": 7, "3": 5}

def msg(text: str, color: str = Fore.WHITE, style: str = Style.NORMAL, end: str = "\n") -> None:
    """Unified print helper with optional color and style."""
    print(style + color + text, end=end)


def get_player_name() -> str:
    return input("What's your name:\n").strip()

def select_difficulty() -> str | None:
    """Ask the user to select difficulty or exit."""
    while True:
        print("\n=== Select Difficulty ===")
        for key, value in DIFFICULTIES.items():
            print(f"{key} -> {value}")
        print("0 -> Exit")

        choice = input(f"Select 1, 2 or 3 (0 to Exit)\n").strip()

        if choice == "0":
            msg("Good bye!\nSee you next time...\n", Fore.CYAN)
            return None

        if choice not in DIFFICULTIES:
            msg("Invalid choice. Please try again.\n", Fore.RED)
            continue

        msg(f"\nYou selected: {DIFFICULTIES[choice]}.\n", Fore.CYAN)
        return choice

def get_word(difficulty: str) -> tuple[str, str]:
    """Pick a random word based on difficulty level."""
    words = {
        "1" : ["Apple", "Duck", "Book", "Rain", "Music"],
        "2" : ["Python", "Planet", "Window", "Thunder" ,"Shadow"],
        "3" : ["Science", "Computer", "Labyrinth", "Building", "Physics"],
    }

    word = random.choice(words[difficulty]).lower()
    msg(f"The word has {len(word)} characters.\n", Fore.CYAN)

    masked_word = "_ " * len(word)
    return word, masked_word

def get_letter():
    """Prompt the user for a valid single-letter guess."""
    while True:
        letter = input(f"Guess a letter:\n").strip().lower()
        if letter.isalpha():
            return letter
        else:
            msg("Invalid input. Please enter only letters (A–Z).", Fore.RED)

def validate_input(letter: str, word: str, masked_word: str) -> str:
    """Validate the guessed letter or full word."""
    usr_input = letter.lower().strip()
    new_masked = ""

    # Full word guess
    if len(usr_input) > 1:
        if usr_input == word:
            msg(f"🎉 Correct! The word was '{word.upper()}'!\n", Fore.BLUE, Style.BRIGHT)
            return word, True, True
        else:
            msg(f"'{letter}' is not the correct word.\n", Fore.RED)
            return masked_word, False, False

    # Single-letter guess
    correct_guess = False
    for w, m in zip(word, masked_word.split()):
        if w == letter:
            new_masked += (w + " ")
            msg(f"That's right! The letter '{letter.upper()}' is in the word.\n", Fore.GREEN)
            correct_guess = True
        else:
            new_masked += (m + " ")

    new_masked = new_masked.strip()
    game_won = "_ " not in new_masked and "_" not in new_masked

    if game_won:
        msg(f"Correct! The word was: {word.upper()}\n", Fore.GREEN, Style.BRIGHT)

    return new_masked, correct_guess, game_won

def play_game(name: str, difficulty: str):
    """Main hangman gameplay loop."""
    word, masked_word = get_word(difficulty)
    lives = LIVES_BY_DIFFICULTY[difficulty]
    guessed_letters = set()

    while True:
        print(HANGMAN_PICS[lives])
        msg(f"{masked_word}\n", Fore.WHITE)
        msg(f"Lives left: {lives}\n", Fore.CYAN)
        msg(f"Guessed letters: {', '.join(sorted(guessed_letters)) or '(none)'}\n", Fore.YELLOW)

        guess = get_letter()

        if guess in guessed_letters:
            msg(f"\nYou already guessed '{guess.upper()}'. Try another letter.\n", Fore.YELLOW)
            continue

        guessed_letters.add(guess)
        masked_word, correct, won = validate_input(guess, word, masked_word)

        if won:
            msg(f"🏆 Congratulations, {name}! You won!\n", Fore.BLUE, Style.BRIGHT)
            break

        if not correct:
            lives -= 1
            msg("\nYour guess is wrong. Try again.\n", Fore.RED)
            if lives == 0:
                print(HANGMAN_PICS[0])
                msg(f"\n💀 You lost! The word was: {word.upper()}.\n", Fore.RED)
                break


def main():
    print(Style.BRIGHT + Fore.BLUE + TITLE)
    name = get_player_name()
    msg(f"\nAlright {name}!\nLet's play Hangman!\n", Fore.BLUE, Style.BRIGHT)

    while True:
        difficulty = select_difficulty()
        if not difficulty:
            sys.exit()  # clean exit from main

        # Fun intro line
        if difficulty == "1":
            msg("I'll be gentle then...\n", Fore.CYAN)
        elif difficulty == "2":
            msg("Not too bad, let's start.\n", Fore.CYAN)
        else:
            msg("You're very brave!\n", Fore.MAGENTA)

        play_game(name, difficulty)

        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            msg("\nThanks for playing! Goodbye 👋\n", Fore.CYAN)
            sys.exit()


if __name__ == "__main__":
    main()
