def input_word() -> str:
    # Prompt the user to enter a 5-character word
    word = input("Enter a 5-character word: ")

    # Check if the input word is not 5 characters long
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")

    # Return the word regardless of its length
    return word
