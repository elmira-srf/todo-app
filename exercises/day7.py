names = ["john smith", "jay santi", "eva kuki"]
print([i.title() for i in names])

usernames = ["john 1990", "alberta1970", "magnola2000"]
print([len(i) for i in usernames])

user_entries = ['10', '19.1', '20']
print([float(i) for i in user_entries])

# user_numbers = [float(i) for i in user_entries]
# print(sum(user_numbers))
print(sum([float(i) for i in user_entries]))