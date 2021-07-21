import random
ABC = "abcdefghijklmnopqrstuvwxyz"
labc = list(ABC)
random.shuffle(labc)
rABC = ''.join(labc)
print(rABC)
message = input().lower()
r = ''
for char in message:
    if char in ABC:
        r+=ABC[rABC.find(char)]
    else:
        r+=char
print(r)
