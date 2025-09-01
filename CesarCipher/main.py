alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Enter 'encode' to encrypt or 'decode' to decrypt: ")

text = input("Enter your message: ").lower()

shift = int(input("Enter the shift number: "))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position =  (alphabet.index(letter) + shift_amount) % len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"The encoded text is {cipher_text}")
    return cipher_text

def decrypt(cipher_text, shift_amount):
    original_text = ""

    for letter in cipher_text:
        shifted_position =  (alphabet.index(letter) - shift_amount) % len(alphabet)
        original_text += alphabet[shifted_position]

    print(f"The decoded text is {original_text}")
    return original_text

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
