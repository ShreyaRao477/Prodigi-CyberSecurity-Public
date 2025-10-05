from PIL import Image
import os

def encrypt_image(image_path, key):
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    encrypted_path = "encrypted_image.png"
    image.save(encrypted_path)
    print(f"\nEncryption complete! Saved as '{encrypted_path}'")

def decrypt_image(image_path, key):
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    decrypted_path = "decrypted_image.png"
    image.save(decrypted_path)
    print(f"\nDecryption complete! Saved as '{decrypted_path}'")

# Main Program
print("=== Simple Image Encryption and Decryption Tool ===\n")

operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
image_path = input("\nEnter image file path (e.g., sample.png): ").strip()
key = int(input("\nEnter numeric key (e.g., 50): "))

if not os.path.exists(image_path):
    print("\nError: Image file not found!")
else:
    if operation == "encrypt":
        encrypt_image(image_path, key)
    elif operation == "decrypt":
        decrypt_image(image_path, key)
    else:
        print("\nInvalid operation! Please type 'encrypt' or 'decrypt'.")
