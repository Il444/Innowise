def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

def get_birth_year():
    while True:
        try:
            birth_year_str = input("Enter your birth year: ").strip()
            birth_year = int(birth_year_str)
            if 1900 <= birth_year <= 2026:
                return birth_year
            print("Please enter a realistic year (e.g. 1995).")
        except ValueError:
            print("Please enter a valid number.")

def main():
    user_name = input("Enter your full name: ")
    current_age = 2026 - get_birth_year()
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == "stop":
            break
        hobbies.append(hobby)

    life_stage = generate_profile(current_age)
    user_profile = {"Name" : user_name, "Age" : current_age, "Life Stage" : life_stage, "Favorite Hobby" : hobbies}

    print("---")
    print("Profile Summary:")
    for key, value in user_profile.items():
        if key == "Favorite Hobby":
            if not value:
                print("You didn't mention any hobbies.")
            else:
                print(f"Favorite hobbies ({len(value)}) :")
                for hobby in value:
                    print(f"- {hobby}")
        else:
            print(f"{key}: {value}")

    print("---")

if __name__ == "__main__":
    main()