import sys

params = sys.argv[1:]

if len(params) == 2:
    try:
        start = int(params[0])
        end = int(params[1])
        if start <= end:
            result = list(range(start, end + 1))
        else:
            result = list(range(start, end - 1, -1))
        print(result)
    except ValueError:
        print("none")
else:
    print("none")