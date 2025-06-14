import random
import string

length=int(input("enter the length of the password : "))
add_upper=input("Include capital letters?(yes/no): ")
add_lower=input("Include small letters?(yes/no): ")
add_numbers=input("Include numbers?(yes/no): ")
add_symbols=input("Include symbols?(yes/no): ")

all_chars = ""
selected_types = []
if add_upper == "yes":
    all_chars += string.ascii_uppercase
    selected_types.append(random.choice(string.ascii_uppercase))

if add_lower=="yes":
    all_chars += string.ascii_lowercase
    selected_types.append(random.choice(string.ascii_lowercase))

if add_numbers == "yes":
    all_chars += string.digits
    selected_types.append(random.choice(string.digits))


if add_symbols == "yes":
    all_chars += string.punctuation
    selected_types.append(random.choice(string.punctuation))

if all_chars == "":
    print("please enter the options")
elif len(selected_types)<2:
    print("please select atleast two character types to make password stronger ")    
elif length< len(selected_types):
    print("length must be at least to include all selected types")
else:
    remaining=[random.choice(all_chars)
for  i in range(length-len(selected_types))]
    password_list=selected_types+remaining
    random.shuffle(password_list)
    password=''.join(password_list)
    print("your strong password is :",password)

