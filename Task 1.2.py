import os

string = str(input("Enter the String: "))
runes = list(string)

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
    

        
