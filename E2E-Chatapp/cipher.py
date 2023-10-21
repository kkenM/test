import random

# Function to convert ASCII character to bits
def char_to_bits(char):
    bits = bin(ord(char))[2:]  # Convert ASCII to binary and remove '0b' prefix
    return bits.zfill(7)  # Add leading zeros to make it 8 bits long

# Function to generate a random 8-bit bitmask
def generate_mask():
    return bin(random.randint(0, 31))[2:].zfill(7)

# Function to apply XOR encryption and decryption
def xor_encrypt(char, mask):
    char_bits = char_to_bits(char)
    encrypted_bits = ''.join([str(int(char_bit) ^ int(mask_bit)) for char_bit, mask_bit in zip(char_bits, mask)])
    return int(encrypted_bits, 2)

# Example usage:
character = ' '  # The character you want to encrypt
mask = generate_mask()  # Generate a random 8-bit bitmask
encrypted_char = xor_encrypt(character, mask)
decrypted_char = xor_encrypt(chr(encrypted_char), mask)

# Function to take a message encrypt it via xor bitmask, returns encrypted message in decimal characters and the bitmasks
def cipher_message(message):

    protected_message = ""
    masks = ""

    for char in message:
        new_mask = generate_mask()

        encrypt_char = xor_encrypt(char, new_mask)

        protected_message += chr(encrypt_char)
        masks += new_mask + " "

    return protected_message, masks

def decipher_message(encrypted_msg, mask_list):

    mask_list = mask_list.split()
    deciphered_msg = ""

    for char, mask in zip(encrypted_msg, mask_list):
        decrypt_char = xor_encrypt(char, mask)
        char = chr(decrypt_char)
        deciphered_msg += char

    return deciphered_msg

