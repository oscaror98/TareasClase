import re
from colorama import Fore
import requests

website = "https://www.flashscore.es/futbol/espana/laliga-ea-sports/clasificacion/#/SbZJTabs/table/overall"
resultado = requests.get(website)
content = resultado.text


patron = r"/futbol/[\w-]*"
equipos_laliga = re.findall(patron, str(content))

sinDuplicados = list(set(equipos_laliga))
equipos_array = []
ligas_array = []
ligaAlemana = []
ligaItaliana = []
ligaEsp = []
for i in sinDuplicados:
    nombres_paises = i.replace("/futbol/","")
    patron2 = r"/futbol/"+ nombres_paises +"/[\w-]*"
    ligas = re.findall(patron2,str(content))
    sinDuplica2 = list(ligas)
   
    for j in sinDuplica2:
        nombres_ligas = j.replace("/futbol/{nombres_paises}/","")
        nombre = []
        nombre = nombres_ligas.split("/")
        if(nombre[3] != ""):
            ligas_array.append(nombre[3].upper())
        if(nombre[2] == "alemania"):
            ligaAlemana.append(nombre[3])
        if(nombre[2] == "italia"):
            ligaItaliana.append(nombre[3])
        if(nombre[2] == "espana"):
            ligaEsp.append(nombre[3])

print("Alemania:")
for x in ligaAlemana :
    print (x.upper())
print(" --- ")
print("Italia:")
for y in ligaItaliana :
    print (y.upper())
print(" --- ")
print("España:")
print()
print(ligaEsp[58].upper())
print(ligaEsp[59].upper())
print(ligaEsp[60].upper())
print(" --- ")





    
