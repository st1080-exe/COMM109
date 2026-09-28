
total = input("Enter the total bill: \n")
people = input("Enter the number of people: \n")
split = round(float(total)/int(people),2)
print(f"Each person should pay {split} so the bill is fully covered (total paid will be {round(split*int(people),2)}).")
