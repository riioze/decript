import os
import io
import json
path='ref.txt'


#create dict
ABC = "abcdefghijklmnopqrstuvwxyz"
dp = {}
for char in ABC:
    dp[char] = {'total' : 0}
    for c in ABC+'.':
        dp[char][c] = 0

#take the text
with io.open(path, 'r',encoding='utf8') as f:
    text = f.read().lower().replace('é','e').replace('è','e').replace('ê','e').replace('à','a').replace('ç','c').replace('ù','u').replace('\n',' ')
    print(text)

#analyse
for x in range(len(text)-2):
    if text[x] in ABC:
        if text[x+1] in ABC:
            dp[text[x]][text[x+1]]+=1
        else:
            dp[text[x]]['.']+=1
        dp[text[x]]['total']+=1
for lettre,ligne in dp.items():

    for c in ABC+'.':
        ligne[c]/=ligne['total']
    print(lettre,ligne)

with open('table.txt','w') as f:
    f.write(json.dumps(dp))
