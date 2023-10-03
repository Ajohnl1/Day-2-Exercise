# Dunder
if __name__ == "__main__":

    user_name = input("What is your name? ")
    user_number = int(input("Enter a number between 1 - 100."))  # Enter Number

    if user_number < 60 and user_number % 2 != 0:  # Less than 60 and Odd number
        str(print(user_number))
        print(user_name + "'s Number is odd and less than 60.")

    elif user_number in range(1,25) and user_number % 2 == 0:  # Even and between range 2 - 24
        print(user_name + "'s number is even and less than 25.")

    elif user_number in range(25,61) and user_number % 2 == 0:  # Even and between 26 and 60
        print(user_name + "'s number is even and between 26 and 60 inclusive.")

    elif user_number > 60 and user_number % 2 == 0:  # Greater than 60 and Even
        print(user_name + "'s number is even and greater than 60.")

    elif user_number > 60 and user_number % 2 != 0:  # Greater than 60 and Odd
        print(user_name + "'s Number is odd and greater than 60.")
