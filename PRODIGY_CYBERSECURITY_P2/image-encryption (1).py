from PIL import Image
import numpy as np
import os

IMAGE_FOLDER = 'images'

def process_image(image_name, key, mode):
    try:
        image_path = os.path.join(IMAGE_FOLDER, image_name)
        
        if not os.path.isfile(image_path):
            print(f"Error: {image_name} not found in the {IMAGE_FOLDER} folder. Please provide a valid file name.")
            return
        
        image = Image.open(image_path)
        image_array = np.array(image)
        processed_image_array = image_array ^ key
        processed_image_array = np.clip(processed_image_array, 0, 255)
        output_image = Image.fromarray(np.uint8(processed_image_array))
        
        output_path = os.path.join(IMAGE_FOLDER, "encrypted_image.png" if mode == 'e' else "decrypted_image.png")
        output_image.save(output_path)
        print(f"Image processed successfully. Saved at: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_valid_key():
    while True:
        try:
            key = int(input("Enter the encryption/decryption key (integer between 0 and 255): "))
            if key < 0 or key > 255:
                raise ValueError("Key must be between 0 and 255.")
            return key
        except ValueError as e:
            print(f"Invalid key. {e}. Please try again.")

def get_image_name_for_processing(mode):
    while True:
        image_name = input(f"Enter the name of the {'encrypted' if mode == 'd' else 'original'} image (e.g., image.png): ").strip()
        if not os.path.isfile(os.path.join(IMAGE_FOLDER, image_name)):
            print(f"Error: {image_name} not found in the {IMAGE_FOLDER} folder. Please provide a valid file name.")
        else:
            return image_name

def main():
    print("Welcome to the Image Encryption and Decryption Program!")
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    while True:
        print("\nOptions: ")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            image_name = get_image_name_for_processing('e')
            key = get_valid_key()
            process_image(image_name, key, 'e')

        elif choice == '2':
            image_name = get_image_name_for_processing('d')
            key = get_valid_key()
            process_image(image_name, key, 'd')

        elif choice == '3':
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
