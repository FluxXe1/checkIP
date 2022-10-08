import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("WELLCOME")
print(ascii_banner)

print("Silahkan Masukan Username Dan Password Untuk Login")

username = "user"
password = "admin"

def login (user_name, pass_word) :
    if user_name != username and pass_word != password :
        hasil = False
    else :
        hasil = True

    return hasil

i=1
while i>=1:
    userName_=input("[+]Username :")
    password_=input("[+]Password :")
    hasil=(login(userName_, password_))
    if hasil == True :
        print ("LOGIN SUCCES")
        print(f" ")
        break
    else :
        i-=0
        print("USERNAME ATAU PASSWORD ANDA SALAH!!" )
        print("MASUKAN DENGAN BENAR!!")
        print(f" ")


ascii_banner = pyfiglet.figlet_format("IP CHECKER")
print(ascii_banner)

import socket
import json
import pprint

hostname = input("[+]MASUKAN DOMAIN: ")

ip_address = socket.gethostbyname(hostname)

requests_url = "https://geolocation-db.com/jsonp/" + ip_address
response = requests.get(requests_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
              pprint.pprint(str(k) + " : " + str(v))
