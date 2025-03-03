# Square Root Calculation Program

def calculate_square_root(number):
  """Calculates the square root of a number.

  Args:
    number: The number to find the square root of.

  Returns:
    The square root of the number, or an error message if the input is invalid.
  """

  if number < 0:
    return "Cannot calculate the square root of a negative number."
  else:
    square_root = number ** 0.5
    return square_root

# Get input from the user (Codingal Specific)
try:
  num = float(input())  # Codingal takes input directly without a prompt
  result = calculate_square_root(num)
  print(result)  # Codingal expects the result to be printed directly
except ValueError:
  print("Invalid input") # Codingal expects very specific outputs.