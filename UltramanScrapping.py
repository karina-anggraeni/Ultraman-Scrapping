## Tugas 10 Desember
## JCAH Data Science
## Karina Anggraeni

#----------------------------------------------------------------------------------------------------------#

from bs4 import BeautifulSoup
import requests
import json

url_ = 'https://www.scifijapan.com/merchandise/bandai-ultraman-ultra-500-figure-list'
web = requests.get(url_)
out_ = BeautifulSoup(web.content, 'html.parser')

# Tarik data
data = []
for i in out_.find_all('strong'):
    data.append(i.text)

# List Ultraman
ultraman_start = data.index('01 Ultraman')
ultraman_end = data.index('34 Ultraman Victory Knight')
ultraman_list = data[ultraman_start : ultraman_end+1]

# List Monster
monster_start = data.index('01 Alien Baltan')
monster_end = data.index('73 Judah Spectre')
monster_list = data[monster_start : monster_end+1]

# Dictionary Ultraman
ultraman_dict = {'ULTRAMAN': {i[0:2] : i[2:len(i)] for i in ultraman_list}}

# Dictionary Monster
monster_dict = {'MONSTER' : {i[0:2] : i[2:len(i)] for i in monster_list}}

# ALL Ultraman +  Monster
ultraman_monster = []
ultraman_monster.append(ultraman_dict)
ultraman_monster.append(monster_dict)

#----------------------------------------------------------------------------------------------------------#

## JSON
with open('ultraman_monster.json', 'w') as file:
    json.dump(ultraman_monster, file)

with open('ultraman_monster.json', 'r') as file:
    output = json.load(file)
print(output)