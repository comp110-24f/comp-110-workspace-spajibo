"""Ex02- Chardle - A cute step toward Wordle."""

__author__ = "730671372"

"I had to resubmit a couple of times because I didn'tunderstand the quit function"


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    # Check if the input word is not 5 characters long
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# this is meant to exit the code before something is returned
def input_letter() -> str:
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


"We return the function as none because we dont need it to return"


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    count = 0

    # Check each index,"count goes up if char is found because it lets user know that the char is in the word"
    if letter == word[0]:
        print(str(letter) + " found at index 0")
        count += 1
    if letter == word[1]:
        print(str(letter) + " found at index 1")
        count += 1
    if letter == word[2]:
        print(str(letter) + " found at index 2")
        count += 1
    if letter == word[3]:
        print(str(letter) + " found at index 3")
        count += 1
    if letter == word[4]:
        print(str(letter) + " found at index 4")
        count += 1

    # Print number of matches found
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    elif count == 1:
        print("1 instance of " + str(letter) + " found in " + str(word))
    else:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


"if count freater than 1 the else will print, I could use another elif"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
