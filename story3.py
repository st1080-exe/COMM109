a = input("Enter number of cages: \n")
b = input("Enter number of animals per cage: \n")
c = input("Enter an adjective (c): ")
d = input("Enter an animal in plural form: ")
e = input("Enter number of food items in the bucket: \n")
f = input("Enter a type of food in plural form: \n")

print(f"""In the zoo there were  {a}  cages each containing  {b}  {c}  {d}.
There were {int(a)*int(b)} {d} in total.
The zoo keeper had a bucket with  {e}  {f}  in. 
They fed each animal {int(e)//(int(a)*int(b))} {f}, putting the  {int(e)%(int(a)*int(b))}  leftover  {f}  in the freezer.""")