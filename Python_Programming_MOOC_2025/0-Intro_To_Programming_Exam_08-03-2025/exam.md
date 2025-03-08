Introduction to Programming, spring 2025, Online Exam 1
March 8th, 2025


Exercise 1
Complete this in exercise template exercise1.py

Please write a program, which ask user to type in numbers one by one. When the user inputs number zero, program outputs:

smallest number
biggest number
amount of the numbers
sum of the numbers
most repeated number
After this, the execution of the program ends.

The example run of the program:


Type in a number: 5
Type in a number: 10
Type in a number: -3
Type in a number: 5
Type in a number: 14
Type in a number: 0
Biggest: 14
Smallest: -3
Number of numbers: 5
Sum: 31
Most repeated: 5
Note! In the example, "Type in a number" is an input query message, and the number following it is an input from the user.

You can make an assumption, that the user inputs at least one number and that the user inputs only valid strings (integers).

Exercise 2
Complete this in exercise template exercise2.py

The task is to create two functions that implement Caesar encryption and decryption: caesar_encrypt(text: str, shift_value: int) and caesar_decrypt(text: str, shift_value: int).

The Caesar cipher is a simple encryption method used by Julius Caesar to encrypt his messages.

The Caesar cipher works by replacing each letter in the text with another letter that is a certain number of positions forward from the original letter in the alphabet. If the letter goes beyond the last letter, it wraps around to the beginning of the alphabet. For example, calling caesar_encrypt with the string "abc" and a shift_value of 2 would return "cde". Similarly, calling caesar_decrypt with the string "cde" and a shift_value of 2 would return "abc".

In this task, you only need to consider lowercase English ASCII letters, in other words: "abcdefghijklmnopqrstuvwxyz". You can assume that the function will not be given strings containing numbers, uppercase letters, special characters, spaces, or anything similar.

The string "zorro" with shift_value 1 would be "apssp" after encryption. Similarily string "apssp" after decryption with shift_value 1 would be "zorro".

Example of using the function caesar_encrypt:


words_to_encrypt = [
    "one",
    "of",
    "the",
    "foods",
    "i",
    "like",
    "is",
    "pizza"
]

for word in words_to_encrypt:
    encrypted = caesar_encrypt(word, 3)
    print(encrypted)
The program outputs:


rqh
ri
wkh
irrgv
l
olnh
lv
slccd
Example of using the function caesar_decrypt:


secret_message = [
"ersxliv", 
"sri", 
"mw", 
"qegevsrm", 
"gewwivspi", 
"figeywi", 
"mx", 
"mw", 
"gliet", 
]

for word in secret_message:
    decrypted = caesar_decrypt(word, 4)
    print(decrypted)
The program outputs:


another
one
is
macaroni
casserole
because
it
is
cheap
You can also make sure that your program is working properly with these function calls. The program should only print True in these tests.


ecrypt_and_decrypt = [
    "message",
    "encrypted",
    "and",
    "decrypted"
    ]
# Becaues the encryption is decrypted with the same shift value as it was encrypted, all the prints are True
for word in ecrypt_and_decrypt:
    encrypted = caesar_encrypt(word, 15)
    decrypted = caesar_decrypt(encrypted, 15)
    print(word == decrypted)

# Test the encryption with 26 as the shift value
# The words should not change because the shift value is the same as the alphabet length

for word in ecrypt_and_decrypt:
    encrypted = caesar_encrypt(word, 26)
    decrypted = caesar_decrypt(word, 26)
    print(word == encrypted == decrypted)
Exercise 3
Complete this in exercise template exercise3.py

Copy the code below into the exercise template.


from fractions import Fraction

def fraction_calculator(calculation: str):
    pass

def convert_to_fraction(fraction: str):
    pass
The Fraction object works in such a way that it takes two values: the first value is the numerator, and the second value is the denominator. For example, a fraction corresponding to half is created as Fraction(1,2). Fractions can also be created from decimals using the Fraction object, but that is not necessary for this exercise.

The task is to program a fraction calculator that an perform following operations:

Addition
Subtraction
Multiplication
Reduction of the fraction, which is automatically done by Fraction object.
Create the program so that the function fraction_calculator calls the function convert_to_fraction. The fraction_calculator function is given a calculation as a string, and it returns the result as a string. The convert_to_fraction function is given a fraction as a string, and it returns a Fraction object.

You can assume, that the value given to the function is always in the format shown in the example below, meaning:

There is no space between the minus sign and the number in a negative fraction.
There is always a space between the number and the operator. For example, 5 + 4 is possible, but 5+4 is not a possible argument for the fraction calculator.
Example of how the convert_to_fraction function works:


fraction = "1/2"
fraction2 = "15/375"
fraction_object = convert_to_fraction(fraction2)
print(convert_to_fraction(fraction))
print(type(fraction_object))
print(fraction_object)
Output of the example:


1/2
<class 'fractions.Fraction'>
1/25
Example of how the fraction_calculator function works:


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
Output of the example:


<class 'str'>
<class 'str'>
the sum of 1/2 + 3/4 is 5/4
the difference of 1/2 - 1/3 is 1/6
the product of -1/2 * 1/4 is -1/8
fraction 15/375 in reduced form is 1/25
5/24
Hint: You can convert a Fraction object to string using str() function
