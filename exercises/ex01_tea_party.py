"This code is for the tea party assignment"

__author__ = "730671372"


# THis function is the entrypoint of my program
# For planner we needed to convert to string bc user should enter a number"
# Whenever I call another function inside of one, I have to add its peramaters and set
# it equal to the current functions paramter


def main_planner(guest: int) -> None:
    """This is the main function of my code"""
    print("A Cozy Tea Party for " + str(guest) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guest)))
    print("Treats: " + str(treats(people=guest)))
    print(
        "Cost: $"
        + str(cost(tea_count=tea_bags(people=guest), treat_count=treats(people=guest)))
    )


def tea_bags(people: int) -> int:
    """Caculates how many tea bags we need"""
    return people * 2


# This functions ask how many people are coming and then doubles it


def treats(people: int) -> int:
    "caculates how many treats we need"
    return int(tea_bags(people=people) * 1.5)


# If I dont add int it will return as a float


def cost(tea_count: int, treat_count: int) -> float:
    "this is the total amount of money"
    return (tea_count * 0.5) + (treat_count * 0.75)


# I had to change my orignal code, before I thought I need to make the amounts new variables and then
# use concatenation and multiplication to get a final result

# I created new variables to hold the amount a treat and cost was. line 35 caculates the
# total cost

if __name__ == "__main__":
    main_planner(guest=int(input("How many guest are attending your tea party:")))
