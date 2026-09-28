print("answer the following questions")
name = input("What is your name?")
phrase = input("What is your favorite phrase?")
age = input("How old are you?")
food = input("What is your favroite food")

print(f"""It was {name.title()}'s first day of school and they wanted to make an impression on people.
The teacher asked them all to stand up and introduce themselves.
{name.title()} said "Hello, my name is {name.title()}. I am {age.lower()} years old. {food.title()} is my favorite food and my favorite phrase is {phrase.upper()}"
The class erupted in laughter and {name.title()} was sent to the principals office""")