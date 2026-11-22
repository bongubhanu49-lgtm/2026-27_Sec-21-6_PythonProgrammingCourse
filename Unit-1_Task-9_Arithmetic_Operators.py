number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

if number2 != 0:
	print(f"Division: {number1 / number2}")
	print(f"Floor division: {number1 // number2}")
	print(f"Modulus: {number1 % number2}")
else:
	print("Division, floor division, and modulus are undefined when the second number is 0.")

print(f"Exponent: {number1 ** number2}")