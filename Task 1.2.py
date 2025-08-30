import os

runes = [
    "a","b","c","d","e","f","g","h","i","j","k","l","x","y","z","m","n","o","p","q",
    "r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k",
    "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e",
    "f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y",
    "z","l","u","m","o","s","a","b","c","d","e","f","g","h","i","j","k","l","m","n"
]

boolean = False

lumos = ["o","s","u","m","l"]

count = 0

for count,i in enumerate(runes):
    for j in lumos:
        if i == j:
            lumos.remove(j)
    if not lumos:
        boolean = True
        break
if boolean == True:
    print(count+1)
else:
    print("-1")
    
        