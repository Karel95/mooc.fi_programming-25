# Write your solution to exercise 3 here

from fractions import Fraction

def fraction_calculator(calculation: str) -> str:
    # Split the calculation into operands and operator
    parts = calculation.split()
    
    if len(parts) == 1:
        # Only one fraction, reduce it
        return str(convert_to_fraction(parts[0]))
    
    fraction1 = convert_to_fraction(parts[0])
    operator = parts[1]
    fraction2 = convert_to_fraction(parts[2])
    
    # Perform the calculation based on the operator
    if operator == '+':
        result = fraction1 + fraction2
    elif operator == '-':
        result = fraction1 - fraction2
    elif operator == '*':
        result = fraction1 * fraction2
    elif operator == '/':
        result = fraction1 / fraction2
    else:
        raise ValueError("Invalid operator")
    
    return str(result)

def convert_to_fraction(fraction: str) -> Fraction:
    # Split the fraction string into numerator and denominator
    numerator, denominator = map(int, fraction.split('/'))
    return Fraction(numerator, denominator)

# Example usage
calculation1 = "1/2 + 3/4"
calculation2 = "1/2 - 1/3"
calculation3 = "-1/2 * 1/4"
to_be_reduced = "15/375"

result_of_addition = fraction_calculator(calculation1)
result_of_subtraction = fraction_calculator(calculation2)
result_of_multiplication = fraction_calculator(calculation3)
reduced = fraction_calculator(to_be_reduced)

print(type(to_be_reduced))
print(type(reduced))

print(f'the sum of {calculation1} is', result_of_addition)
print(f'the difference of {calculation2} is', result_of_subtraction)
print(f'the product of {calculation3} is', result_of_multiplication)
print(f'fraction {to_be_reduced} in reduced form is', reduced)

# We'll calculate (1/2 + 3/4) * (1/2 - 1/3) using the results of the previous calculations
calculation4 = f"{result_of_addition} * {result_of_subtraction}"
print(fraction_calculator(calculation4))
