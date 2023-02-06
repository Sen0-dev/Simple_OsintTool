import sys
import re
import requests
import json

"""
Vous allez ici créer votre premier outil de reconnaissance passive, vous avez le choix de la langue, cependant votre programme devra reconnaître les informations saisies (FULL NAME, IP, @login).

- Pour le cas du nom complet, il devra reconnaître l'entrée : Nom Prénom, puis chercher dans les annuaires le numéro de téléphone et l'adresse.

- S'il s'agit de l'adresse ip, votre outil devrait afficher au moins la ville et le nom du fournisseur d'accès internet.

- S'il s'agit d'un nom d'utilisateur, votre outil devra vérifier si ce nom d'utilisateur est utilisé dans au moins 5 réseaux sociaux connus.

Le résultat doit être stocké dans un fichier result.txt (result2.txt si le fichier existe déjà).
"""


# ------ Search Functions ------

def Help():
    print("""
        passive --help

        Welcome to passive v1.0.0

        OPTIONS:
            -fn         Search with full-name
            -ip         Search with ip address (127.0.0.1 or public address, V4 only)
            -u          Search with username
    """)
    exit(0)


def ByFn(full_nameLIST):

    full_name = " ".join(full_nameLIST)


    


def ByIp(user_ipLIST):

    user_ip = " ".join(user_ipLIST)
    ip = user_ip

    if ip == "127.0.0.1":
        ip = requests.get("http://api.myip.com").json()["ip"]

    ipwhoResponse = requests.get('http://ipwho.is/'+ip)
    data = ipwhoResponse.json()

    print(f"""
    ISP: {data["connection"]["isp"]}
    City Lat/Lon: {data["city"]}
    """)



def ByUsername(usernameLIST):

    username = " ".join(usernameLIST)
    social_networks = ["instagram", "twitter", "tiktok", "facebook", "linkedin"]

    for social_network in social_networks:

        if requests.get("https://www."+ social_network +".com/"+ username).status_code == 200: 
            print(f"{social_network} : yes")
        else:
            print(f"{social_network} : no")



# ------ Check User Entry ------

def CheckFn(full_nameLIST):
    full_name = " ".join(full_nameLIST)
    result = re.search(r"^[a-zA-Z- ]+$", full_name)

    # si ce n'est pas None (qu'il y a un probleme)
    return result is not None


def CheckIp(user_ipLIST):
    user_ip = " ".join(user_ipLIST)
    result = re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", user_ip)

    return result is not None



# ------------ MAIN ------------


# ------ Valid arg ------

args = sys.argv

flags = ["-fn", "-ip", "-u", "--help"]

if len(args) < 2 or args[1] not in flags:
    exit(f"CHOICE AN OPTION {flags} \n")

elif args[1] == flags[len(flags)-1]:
    Help()



# ------ Test entry ------
entry = args[2:]

print(entry)


match args[1]:

    case "-fn":
        if CheckFn(entry) != True:
            exit("A valid full name must not contain symbol or digit, except for a dash \n")
        ByFn(entry)

    case "-ip":
        if CheckIp(entry) != True:
            exit("Enter a valid IP  https://fr.wikipedia.org/wiki/IPv4 \n")
        ByIp(entry)

    case "-u":
        ByUsername(entry)
