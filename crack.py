import os
import json
import random

def pfr(message,table):
    p=0
    for x in range(len(message)-2):
        if message[x] in ABC:
            if message[x+1] in ABC:
                p+=table[message[x]][message[x+1]]/(len(message)-1)
    return p
def evaluate(message,key,table):
    r = ''
    for char in message:
        if char in ABC:
            r+=key[ABC.find(char)]
        else:
            r+=char

    return r,pfr(r,table)



ABC = "eaisnrtoludcmpgbvhfqyxjkwz"

message = input().lower().replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c')
listel = []
for lettre in ABC:
    listel.append((lettre,message.count(lettre)))



listel = [l[0] for l in sorted(listel,key=lambda x: x[1])]
key = ''.join(listel)

with open('table.txt','r') as f:
    table = json.loads(f.read())


trad,p = evaluate(message,key,table)

while p<.9:
    newABC = list(key)
    l1,l2 = [random.choice(ABC) for x in range(2)]
    p1,p2 = [key.find(l) for l in [l1,l2]]
    newABC[p1] = l2
    newABC[p2] = l1
    trad,np = evaluate(message,newABC,table)
    if np > p or (random.random()*np < 0.00001):
        p = np
        key = ''.join(newABC)
        print(f'{key} : {trad} : {p}')
