# Function to convert a string into a hexadecimal representation
def str_to_hex(s):
    return ''.join(f'{ord(c):02x}' for c in s)  # Convert each character to its ASCII value and format it as a two-digit hex string

# Function to convert a hexadecimal string back to a normal string
def hex_to_str(h):
    return ''.join(chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2))  # Convert each pair of hex digits back to a character

# Function to encrypt a plaintext message using a One-Time Pad (OTP) method
def otp_encrypt(plaintext):
    # Generate a pseudo-random key for encryption (deterministic for this implementation)
    key = ''.join(chr((ord(c) * 7) % 256) for c in plaintext)  # Each character is transformed using a simple formula
    # XOR each character in the plaintext with the corresponding character in the key to create the ciphertext
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    # Convert the ciphertext and key to hexadecimal format for safe storage or transmission
    return str_to_hex(ciphertext), str_to_hex(key)

# Function to decrypt a ciphertext back into plaintext using the provided key
def otp_decrypt(ciphertext_hex, key_hex):
    # Convert the hex-encoded ciphertext and key back to their original string format
    ciphertext = hex_to_str(ciphertext_hex)
    key = hex_to_str(key_hex)
    # XOR each character in the ciphertext with the corresponding character in the key to recover the plaintext
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return plaintext

# Main loop to provide a menu-driven interface for encryption and decryption
while True:
    print("Enter 1 to encrypt")
    print("Enter 2 to decrypt")
    print("Enter 3 to quit")
    
    choice = input()  # Take user input for choice selection
    
    if choice == '1':  # Encryption option
        plain_text = input("Enter text: ")  # Get the plaintext input from the user
        cipher, key = otp_encrypt(plain_text)  # Encrypt the plaintext
        print(f"Ciphertext: {cipher}\nKey: {key}")  # Display the encrypted ciphertext and key
    
    elif choice == '2':  # Decryption option
        cipher = input("Enter the cipher code: ")  # Get the encrypted text (ciphertext) from the user
        key = input("Enter the key: ")  # Get the key from the user
        print(f"Decrypted: {otp_decrypt(cipher, key)}")  # Decrypt the ciphertext and display the original text
    
    elif choice == '3':  # Exit option
        break  # Exit the loop and terminate the program
    
    else:  # Handle invalid input
        print("Enter a proper choice")  # Inform the user about an incorrect choice
