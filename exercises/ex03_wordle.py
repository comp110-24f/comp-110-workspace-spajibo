"""This code is meant to run just as the game wordle would"""

___author__ = "730671372"


def input_guess(secret_word_len: int) -> str:
    """Prompts the user for a guess and ensures the guess matches the secret word length."""
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again.")


"""A string that is being searched through for occurences of the second parameter.
A string that is expected to be a single character in length and is the character being searched for"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the character 'char_guess' is found in 'secret_word'."""
    assert len(char_guess) == 1  # Ensure the second parameter is a single character
    i = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


"""This function will return different colo emojis based on the users guess"""


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess1: str, secret: str) -> str:
    assert len(guess1) == len(secret)
    # The next lines will be the if statements that detemine the color of the box/emoij
    result = ""  # this will be the combination of emojis needed
    i = 0  # empty index that will be added to

    while i < len(secret):
        if guess1[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess1[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def main(secret: str) -> None:
    """THe entrypoint of the program and main game loop."""

    max_turns = 6
    turn = 1
    secret_word_len = len(secret)

    # Main game loop
    while turn <= max_turns:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(secret_word_len)
        # The user is asked for a guess, and the input is validated to ensure it is the correct length.
        result = emojified(guess, secret)
        # The guess is compared with the secret word & is stored in result.
        print(result)

        if guess == secret:
            print(f"You won in {turn}/{max_turns} turns!")
            return

        turn += 1

    # If the user runs out of turns without guessing correctly
    print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
