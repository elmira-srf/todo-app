password = input("Enter your password: ")
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
        break
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)
if all(result.values()):
    print("Strong password")
else:
    print("Weak password")