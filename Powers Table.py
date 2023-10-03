# Dunder
if __name__ == "__main__":

    keep_running = True
    while keep_running == True:
        print("Learn your squares and cubes!")  # Opening Statement

        number = int(input("Enter an integer"))  # User Input

        print(f'{"Number":>6}\t{"Square":>8}\t{"Cube":>6}')  # Table formatting

        for i in range(1, number + 1):  # Math Table for squared and cubed
                square = i ** 2
                cubed = i ** 3
                print(f'{i:>6}\t{square:>8}\t{cubed:>6}')  # Table Formatting

        choice = input("Do you want to continue? y/n")
        if choice == "n":
            keep_running = False
