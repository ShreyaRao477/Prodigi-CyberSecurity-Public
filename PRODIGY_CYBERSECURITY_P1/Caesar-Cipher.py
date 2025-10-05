print("Welcome to the Caesar Cipher program!")

def encrypt_decrypt_message(message, shift, action):
    result = []
    
    for char in message:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift_amount = shift if action == 'e' else -shift
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def get_shift_value():
    while True:
        try:
            shift = int(input("Enter the shift value (positive integer): ").strip())
            if shift < 0:
                raise ValueError("Shift value must be a positive integer.")
            return shift
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer.")

def main():
    while True:
        action = input("Please select an option: 'e' for encryption or 'd' for decryption: ").strip().lower()
        if action in ['e', 'd']:
            break
        print("Invalid selection. Please choose 'e' for encryption or 'd' for decryption.")

    message = input("Enter the message: ").strip()
    shift = get_shift_value()
    
    result = encrypt_decrypt_message(message, shift, action)
    
    action_result = "Encrypted" if action == 'e' else "Decrypted"
    print(f"\n{action_result} message: {result}")

if __name__ == "__main__":
    main()
