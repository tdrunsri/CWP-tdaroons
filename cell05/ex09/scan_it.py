import sys

params = sys.argv[1:]

if len(params) == 2 and params[0] in params[1]:
    count = params[1].count(params[0])
    print(count)
else:
    print("none")