def convert(liters):
    return liters/1000

# liters = input("Enter liters: ")
# meters = convert(float(liters))
# print(f"{liters} liters is equal to {meters} cubic meters")


password = input("Enter new password: ")

def pass_stregth(password):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        # result.append(i.isdigit())
        if i.isdigit():
            digit = True
    result["digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["uppercase"] = uppercase

    return result

result = pass_stregth(password)
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")