
turn = 0
heads = 0
while True:
    ht = input("Throw the coin and enter head or tail here: ?")
    turn = turn + 1
    if ht == "head":
        heads = heads + 1
    print(f"Heads : {float(100*heads/turn)}%")
    with open("user_input.txt") as file:
        user_inputs = file.readlines()
        user_inputs.append(ht + "\n")
    with open("user_input.txt", 'w') as file:
        file.writelines(user_inputs)