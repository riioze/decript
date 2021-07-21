import random
ABC = "abcdefghijklmnopqrstuvwxyz"
labc = list(ABC)
random.shuffle(labc)
rABC = ''.join(labc)
print(rABC)
message = input().lower().replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c')
r = ''
for char in message:
    if char in ABC:
        r+=ABC[rABC.find(char)]
    else:
        r+=char
print(r)
