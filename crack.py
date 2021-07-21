

ABC = "abcdefghijklmnopqrstuvwxyz"
labc = list(ABC)
random.shuffle(labc)
key = ''.join(labc)
message = input().lower().replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c')
p=0
while p <.9:



def evaluate(message,key):
    r = ''
    for char in message:
        if char in ABC:
            r+=key[ABC.find(char)]
        else:
            r+=char

    return r,p

def pfr(message):
    pass
