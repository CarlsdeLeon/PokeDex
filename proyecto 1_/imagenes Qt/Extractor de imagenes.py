import requests
import os

for i in range(1, 1026):
    os.system('cls')
    url = ('https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' + str(i) + '.png')
    response = requests.get(url)
    with open("poke" + str(i) + ".jpg", "wb") as f:
        f.write(response.content)
    print("poke" + str(i) + ".jpg")


