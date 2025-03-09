# Write your solution to exercise 2 here

def caesar_encrypt(text: str, shift_value: int) -> str:
    encrypted_text = ""
    for char in text:
        # Shift character and wrap around if necessary
        encrypted_char = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
        encrypted_text += encrypted_char
    return encrypted_text

def caesar_decrypt(text: str, shift_value: int) -> str:
    decrypted_text = ""
    for char in text:
        # Shift character back and wrap around if necessary
        decrypted_char = chr((ord(char) - ord('a') - shift_value) % 26 + ord('a'))
        decrypted_text += decrypted_char
    return decrypted_text

# Test the functions with provided examples
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

# Ensure the program is working properly with these function calls
ecrypt_and_decrypt = [
    "message",
    "encrypted",
    "and",
    "decrypted"
]

# Because the encryption is decrypted with the same shift value as it was encrypted, all the prints are True
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
