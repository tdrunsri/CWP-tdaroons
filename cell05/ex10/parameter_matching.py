import sys

params = sys.argv[1:]

if len(params) == 1:
    user_input = input("What was the parameter? ")
    if user_input == params[0]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")