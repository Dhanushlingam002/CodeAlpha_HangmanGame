import random

WORDS = ["python", "hangman", "keyboard", "monitor", "program"]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAX_WRONG = 6


def display_board(wrong_guesses: int, guessed_letters: set, word: str) -> None:
    """Print the current hangman stage, guessed letters, and masked word."""
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\n  Wrong guesses left : {MAX_WRONG - wrong_guesses}")
    print(f"  Letters guessed    : {' '.join(sorted(guessed_letters)) or '—'}")

    display_word = "  " + " ".join(
        letter if letter in guessed_letters else "_" for letter in word
    )
    print(f"\n  Word : {display_word}\n")


def get_valid_input(guessed_letters: set) -> str:
    """Prompt the player until a valid, unused single letter is entered."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter (a–z).")
        elif guess in guessed_letters:
            print("  ⚠  You already guessed that letter. Try another.")
        else:
            return guess


def play_hangman() -> None:
    """Run one full round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters: set = set()
    wrong_guesses = 0

    print("\n" + "=" * 45)
    print("       Welcome to CodeAlpha Hangman! 🎮")
    print("=" * 45)
    print(f"  A {len(word)}-letter word has been chosen. Good luck!\n")

    while wrong_guesses < MAX_WRONG:
        display_board(wrong_guesses, guessed_letters, word)

        if all(letter in guessed_letters for letter in word):
            print(f"  🎉  You won! The word was '{word.upper()}'.")
            break

        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"  ✅  '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            print(f"  ❌  '{guess}' is NOT in the word.\n")
    else:
        display_board(wrong_guesses, guessed_letters, word)
        print(f"  💀  Game over! The word was '{word.upper()}'.")

    print("=" * 45 + "\n")


def main() -> None:
    while True:
        play_hangman()
        again = input("  Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
