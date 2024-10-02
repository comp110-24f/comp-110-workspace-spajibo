__author__ = "730671362"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    i = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count += 1
        i += 1
    return count


num_instances(phrase="seton", search_char="s")
