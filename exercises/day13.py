def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth

year_of_birth = int(input("What is your year of birth? "))

age = calculate_age(year_of_birth)

if age >= 120:
    print("WOo0W!")
else:
    print(f"You are {age} year old")


def number_of_names(names):
    names_list = names.split(",")
    return len(names_list)

print(number_of_names(input("Enter names separated by commas (no spaces): ")))