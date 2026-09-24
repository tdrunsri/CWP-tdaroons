num_str = input("give me num: ")

val = float(num_str)
if val.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
