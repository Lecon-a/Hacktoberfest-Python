# This script implements binary to decimal conversion.
def bin_to_dec(n) -> int:
    """Convert a binary number (as an integer) to decimal."""
    # Handle baseline cases
    if n < 0:
        raise ValueError("Negative numbers are not supported.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Initialize variables
    base = 2
    bit_len = int(len(str(n))) - 1
    result = 0
    # enumerate through the bits and calculate the decimal value 
    # by raising each element to the power of its index
    for i, n in enumerate(str(n)[::-1]):
        # Convert character to integer
        if n not in ("0", "1"):
            raise ValueError("Input is not a binary number.")
        result += int(n) * (base**i)
    return result

if __name__ == "__main__":
    # Get user input
    try:
        num = int(input("Enter a decimal number: "))
        print(f"Decimal of {num} base 2 is {bin_to_dec(num)}")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")