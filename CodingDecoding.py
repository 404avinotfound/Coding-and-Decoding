import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

def main():
    while True:
        print("Choose an option:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plain_text = input("Enter a message to encrypt: ")
            cipher_text = ""
            for letter in plain_text:
                index = chars.index(letter)
                cipher_text += key[index]

            print(f"original message : {plain_text}")
            print(f"encrypted message: {cipher_text}")
        elif choice == '2':
            cipher_text = input("Enter a message to decrypt: ")
            plain_text = ""

            for letter in cipher_text:
                index = key.index(letter)
                plain_text += chars[index]

            print(f"encrypted message: {cipher_text}")
            print(f"original message : {plain_text}")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
