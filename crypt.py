import random
ABC = "abcdefghijklmnopqrstuvwxyz"
def crypt(message,key):
    r = ''
    for char in message:
        if char in ABC:
            r+=ABC[key.find(char)]
        else:
            r+=char
    return r

if __name__ == '__main__':

    labc = list(ABC)
    random.shuffle(labc)
    rABC = ''.join(labc)
    print(rABC)
    message = input().lower().replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c')
