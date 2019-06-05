print("What's your weight? ")
weight = int(input("Weight: "))
select = input("(L)bs or (K)g: ")
if select.upper() == "L":
    weight = weight * 0.45
    print(f"You are {weight} kilograms")
elif select.upper() == "K":
    weight = weight * 2.2
    print(f"You are {weight} pounds")
else:
    print("Please type a right unit!")