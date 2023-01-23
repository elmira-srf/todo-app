from bonus.parsers14 import parse, convert

feet_inches = input("Enter feet and inches: ")

# result = convert(parse(feet_inches))
parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")
if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slid")
