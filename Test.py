def calculate_square(number):
    """Calculate the square of a number."""
    return number ** 2

def main():
    # Get user input
    user_input = input("Enter a number to square: ")
    try:
        number = float(user_input)  # Convert the input to a floating point number
        result = calculate_square(number)
        print(f"The square of {number} is {result}.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
