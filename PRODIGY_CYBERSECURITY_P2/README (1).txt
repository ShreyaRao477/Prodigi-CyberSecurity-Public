Image Encryption and Decryption Program
========================================

Description:
-------------
This is a Python program that allows users to encrypt and decrypt images using an XOR operation with a provided key. It uses the Python Imaging Library (PIL) and NumPy for image manipulation.

Features:
---------
- Encrypt an image using a key.
- Decrypt an image using the same key.
- Handles images in PNG format.
- Simple command-line interface for user interaction.

Requirements:
-------------
- Python 3.x
- PIL (Pillow) library
- NumPy library

Installation:
-------------
1. Install Python 3.x if not already installed.
2. Install required libraries:
   - Open your terminal/command prompt.
   - Run the following commands:
     ```
     pip install Pillow
     pip install numpy
     ```

How to Use:
------------
1. Place the Python script and the image you want to encrypt/decrypt in the same folder.
2. Run the program by executing the script in your terminal/command prompt:
3. The program will prompt you with options:
- **1**: Encrypt an Image
- **2**: Decrypt an Image
- **3**: Quit

4. For encryption or decryption:
- Provide the name of the image file (e.g., `image.png`) that is in the same folder.
- Enter the encryption/decryption key (integer between 0 and 255).
- The processed image will be saved as `encrypted_image.png` or `decrypted_image.png` in the same folder.

Sources:
--------
- GitHub: https://github.com/dhairya-gayakwad/Prodigy-InfoTech
- Google
