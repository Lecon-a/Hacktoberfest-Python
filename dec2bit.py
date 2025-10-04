# This script implements decimal to binary conversion.

def dec_to_bin(n: int) -> str:
    """Convert a decimal number to binary string."""
    # Handle baseline cases
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    # Initialize variables
    divisor = 2
    result = ""
    # Conversion loop
    while n > 0:
        # Get remainder and quotient
        remainder = n % divisor
        n = n // divisor
        print(f"Remainder: {remainder}, Quotient: {n}")
        result += str(remainder) 

    return result[::-1]  # Reverse the result string


# Example usacase
if __name__ == "__main__":
    # Get user input
    try:
        num = int(input("Enter a decimal number: "))
        print(f"Binary of {num} is {dec_to_bin(num)}")
    except ValueError:
        # Handle invalid input
        print("Please enter a valid integer.")
