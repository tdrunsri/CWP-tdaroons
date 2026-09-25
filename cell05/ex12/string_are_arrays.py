import sys

params = sys.argv[1:]

if len(params) == 1 and 'z' in params[0]:
    count_z = params[0].count('z')
    print('z' * count_z)
else:
    print("none")