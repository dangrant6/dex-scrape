from bs4 import BeautifulSoup
import requests
import sys
import re

#get name
if len(sys.argv) < 2:
	pokemon = input("Enter pokemon name search for: ").title()
elif len(sys.argv) == 3:
	pokemon = (sys.argv[1] + " " + sys.argv[2]).title()
else:
	pokemon = sys.argv[1].title()

#Get dex number
begin_url = "https://www.serebii.net/pokedex-swsh/"
request1 = requests.get(begin_url)
html1 = request1.content
soup1 = BeautifulSoup(html1, "html.parser")
page_info1 = soup1.get_text()
pokemon_index = page_info1.find(pokemon, 5000)
if pokemon_index == -1:
	print("Not a pokemon or mispelled!")
	sys.exit()
pokedex_number = page_info1[pokemon_index-4: pokemon_index-1]

#poke info
full_url = begin_url + pokedex_number + ".shtml"
request2 = requests.get(full_url)
html2 = request2.content
soup2 = BeautifulSoup(html2, "html.parser")
page_info2 = soup2.get_text()

#stats
base_total = soup2.find(string=re.compile("Base Stats - Total:"))
base_total = base_total[base_total.find("Total"):]
base_stats = soup2.find_all(class_="fooinfo")

hp = str(base_stats[len(base_stats)-21])
atk = str(base_stats[len(base_stats)-20])
defence = str(base_stats[len(base_stats)-19])
sp_atk = str(base_stats[len(base_stats)-18])
sp_def = str(base_stats[len(base_stats)-17])
speed = str(base_stats[len(base_stats)-16])

hp = hp[hp.find(">")+1: hp.find("/")-1]
atk = atk[atk.find(">")+1: atk.find("/")-1]
defence = defence[defence.find(">")+1: defence.find("/")-1]
sp_atk = sp_atk[sp_atk.find(">")+1: sp_atk.find("/")-1]
sp_def = sp_def[sp_def.find(">")+1: sp_def.find("/")-1]
speed = speed[speed.find(">")+1:speed.find("/")-1]

#abilities
abil_index = page_info2.find("Abilities:")
abilities = page_info2[abil_index:]
end_index = abilities.find("\n")
abilities = abilities[:end_index-1]

#print
print("Name: ", pokemon)
print("Pokedex Number: ", pokedex_number)
print(abilities)
print("---Base Stats---")
print(base_total)
print("Hp: ", hp)
print("Attack: ", atk)
print("Defence: ", defence)
print("Special Attack: ", sp_atk)
print("Special Defence: ", sp_def)
print("Speed: ", speed)

