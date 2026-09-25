import sys

params = sys.argv[1:]

if len(params) >= 2:
    for param in reversed(params):
        print(param)
else:
    print("none")