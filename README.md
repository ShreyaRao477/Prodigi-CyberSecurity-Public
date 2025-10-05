
Security Tools Collection

Overview

Welcome to the collection of security-related tools.
This suite contains several Python programs for encryption password strength checking, keylogging ,packet sniffing, and image encryption/decryption.

These tools are intended for educational purposes only and should be used ethically and legally, with explicit permission to monitor or manipulate data.

Included Programs

1. Caesar Cipher Program
2. Image Encryption and Decryption Program
3. Password Strength Checking Tool
4. Keylogger Program
5. Packet Sniffer Tool


Prerequisites

Before running the programs, ensure the following Python libraries are installed:

* Pillow (PIL) – Image manipulation
* NumPy – Numerical operations
* Pynput – Capturing keyboard events
* Scapy – Packet sniffing
* Matplotlib – Graphical visualizations
* re, os, sys, time – System operations

Installation Command

```bash
pip install Pillow numpy pynput scapy matplotlib
```

---

1. Caesar Cipher Program

Description

Encrypts and decrypts messages using the Caesar Cipher technique with a user-provided shift value.

Usage

1. Run the program.
2. Choose `'e'` for encryption or `'d'` for decryption.
3. Enter the message to encrypt or decrypt.
4. Provide a positive integer shift value.
5. The program outputs the transformed message.

Dependencies

Python 3.x

Warning

The Caesar Cipher is not secure and is intended for educational purposes only It is vulnerable to simple cryptanalysis.

Sources:GitHub | Google

---

2. Image Encryption and Decryption Program

Description

Encrypts and decrypts images using an **XOR operation** with a numeric key. Utilizes **Pillow** and **NumPy**.

Usage

1. Run the program.
2. Choose the operation (encrypt/decrypt).
3. Provide:

   * The image file (PNG format)
   * An encryption key (integer between 0–255)
4. The result is saved as:

   * `encrypted_image.png` or `decrypted_image.png`

Requirements

* Python 3.x
* Pillow
* NumPy

Warning

XOR image encryption is **not secure** for sensitive data and should only be used **for learning or demonstration**.

**Sources:** GitHub | Google

---

3. Password Strength Checking Tool

Description

Analyzes password strength based on multiple criteria and provides suggestions for improvement.

Usage

1. Run the program.
2. Input a password.
3. Choose to:

   * Check strength
   * View suggestions
   * Examine complexity

Evaluation Criteria

* Minimum 8 characters
* Contains numbers
* Contains uppercase & lowercase letters
* Contains special characters

Warning

This tool is **not foolproof** and should not be the only measure for password protection.

**Sources:** GitHub | Google

---

4. Keylogger Program

⚠️ Disclaimer

This program is for **educational purposes only**.
Use **only with explicit permission** on systems you own or manage. Unauthorized use is **illegal**.

### **Usage**

1. Accept the disclaimer.
2. Enter duration for logging keystrokes.
3. Keystrokes are saved in `keylogger_log.txt`.

### **Menu Options**

* View log file path
* Display log contents
* Learn about legal and ethical considerations
* Quit the program

Important Warning

Keyloggers can capture sensitive data (e.g., passwords). Use **ethically** and **legally**.

**Sources:** GitHub | Google

---

5. Packet Sniffer Tool

Description

Captures network packets for specified protocols (**TCP**, **UDP**, or both**) and allows graphical analysis of results.

Usage

1. Run the script.
2. Accept the disclaimer.
3. Choose protocol and sniffing duration.
4. Captured data is saved in `packet_sniffer_results.txt`.

Dependencies

* Python 3.x
* Scapy
* Matplotlib

Warning

Packet sniffing can reveal confidential data.
Use only on networks where you have **explicit authorization**. Unauthorized monitoring is illegal.

**Sources:** GitHub | Google

---

## **Important Notes**

* Use these tools **only with explicit permission**.
* Any **malicious or unethical use** is strictly prohibited.
* The author is **not responsible** for misuse or damages.

---

## **Author**

**Created by:** Shreya Rao
**GitHub:** https://github.com/ShreyaRao477

**LinkedIn:** https://www.linkedin.com/in/shreya-rao12

### **Acknowledgments**

* Pillow (PIL)
* NumPy
* Pynput
* Scapy
* Matplotlib
* re, os, sys, time

---

## **License**

**MIT License**

© 2025 *Alva’s Institute of Engineering and Technology*

Permission is granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

> Disclaimer:The software is provided "as is", without warranty of any kind.
> The authors are not liable for any claim, damages, or other liabilities arising from its use.

