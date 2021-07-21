ABC = "abcdefghijklmnopqrstuvwxyz"
key = input()
message = input().lower()

r = ''
for char in message:
    if char in ABC:
        r+=key[ABC.find(char)]
    else:
        r+=char
print(r)
