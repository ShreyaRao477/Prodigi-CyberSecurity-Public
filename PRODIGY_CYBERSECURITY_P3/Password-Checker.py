import re

def check_criteria(password):
    has_numbers = any(char.isdigit() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_lower_case = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    return {
        "length": meets_length_requirement,
        "numbers": has_numbers,
        "upper_case": has_upper_case,
        "lower_case": has_lower_case,
        "special_chars": has_special_characters
    }

def assess_password_strength(password):
    criteria = check_criteria(password)
    criteria_met = sum(criteria.values())

    if criteria_met == 5:
        return "Password Strength Level: Very Strong (All criteria are met).", True, criteria
    elif criteria_met == 4:
        return "Password Strength Level: Strong (4 out of 5 criteria are met).", True, criteria
    elif criteria_met == 3:
        return "Password Strength Level: Moderate (3 out of 5 criteria are met).", False, criteria
    else:
        return "Password Strength Level: Weak (Less than 3 criteria are met).", False, criteria

def display_security_tips():
    print("------------------ Password Complexity Checking Tool ------------------")
    print("Here are some quick tips for creating a secure password:")
    tips = [
        "1. Length: Aim for at least 12 characters.",
        "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words: Don't use easily guessable information.",
        "4. No Personal Info: Avoid using names, birthdays, or personal details.",
        "5. Use Passphrases: Consider combining multiple words or a sentence.",
        "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
        "7. Regular Updates: Change passwords periodically.",
        "8. Enable 2FA: Use Two-Factor Authentication where possible.",
        "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
        "10. Password Manager: Consider using one for secure and unique passwords."
    ]
    for tip in tips:
        print(tip)
    print("\n")

def mask_password(password):
    if len(password) > 2:
        return password[0] + '#' * (len(password) - 2) + password[-1]
    return password

def provide_improvement_suggestions(criteria):
    suggestions = []
    if not criteria["length"]:
        suggestions.append("- Increase the password length to at least 12 characters.")
    if not criteria["numbers"]:
        suggestions.append("- Add at least one number.")
    if not criteria["upper_case"]:
        suggestions.append("- Include at least one uppercase letter.")
    if not criteria["lower_case"]:
        suggestions.append("- Include at least one lowercase letter.")
    if not criteria["special_chars"]:
        suggestions.append("- Add at least one special character.\n")
    
    return suggestions

def check_password_complexity(criteria):
    met_criteria_count = sum(criteria.values())
    return f"Password Complexity: {met_criteria_count}/5 criteria met."

def display_menu():
    print("\nChoose an option:")
    print("1. Check Password Strength")
    print("2. View Suggestions for Strengthening Password")
    print("3. View Password Complexity")
    print("4. Quit")

def main():
    display_security_tips()
    
    while True:
        password_input = input("Enter your password: ")
        masked_password = mask_password(password_input)
        result, is_strong, criteria = assess_password_strength(password_input)
        
        print("\nEntered Password: {}".format(masked_password))
        print(result)

        if not is_strong:
            print("\nSuggestions for Improvement:")
            for suggestion in provide_improvement_suggestions(criteria):
                print(suggestion)

        print(check_password_complexity(criteria))

        display_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            print(result)
        elif choice == '2':
            print("\nSuggestions for Improvement:")
            for suggestion in provide_improvement_suggestions(criteria):
                print(suggestion)
        elif choice == '3':
            print(check_password_complexity(criteria))
        elif choice == '4':
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
