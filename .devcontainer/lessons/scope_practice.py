"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty string to copy values over
    index: int = 0  # local variables : copy,index,msg,char
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index] == char):  # if msg[index] != char
            # add it to copy
            copy = copy + msg[index]  # copy += msg[index]
        index += 1  # index = index + 1
    return copy


# creat a variable called word with the value yoyo
word = "yoyo"  # Global variable
# print the result of calling your function arguments word and "y"
print(remove_chars(word, "y"))  # postitional arguements
# print the result of calling your function arguments word and "o"
#print(remove_chars(word, "o"))  # keyword arguemts
