import random
import time
import os
import sys
import colorama
from colorama import Fore 
from colorama import init

os.system("title Onion Link Generator")

chars = "1234567890abcdefghijklmnoprstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM"
start_link_1 = ("http://")
start_link_2 = ("https://")
end_link = (".onoin")

file = open ("links.txt", "w", encoding="utf-8")

time.sleep(2)

print(Fore.BLUE)

print("""
   ____        _               _      _       _    
 / __ \      (_)             | |    (_)     | |   
| |  | |_ __  _  ___  _ __   | |     _ _ __ | | __
| |  | | '_ \| |/ _ \| '_ \  | |    | | '_ \| |/ /
| |__| | | | | | (_) | | | | | |____| | | | |   < 
 \____/|_| |_|_|\___/|_| |_| |______|_|_| |_|_|\_\
                                                  
                                                  
  _____                           _             
 / ____|                         | |            
| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   

""")

print("хотите ли вы сохранять ссылки в .txt [y/n]")

path_to_script = os.path.abspath(os.curdir)

answer = "n"
answer = input()

print("введите колиество ссылок для генерации")

amount = int(input())

starter = input("http = 1 or https = 2: ")

try:
  os.system("cls")
except:
  os.system("clear")

for x in range( amount ):
  if starter == ('1'):
    random_start_link = start_link_1
  elif starter == ('2'):
    random_start_link = start_link_2

  links = ""

  for i in range( 56 ):
    links += random.choice( chars )

  ready_link = random_start_link+links+end_link

  print(Fore.GREEN)
  
  print(ready_link)

  if(answer == "y"):
    file.write(ready_link + '\n')

file.close()
print("\n ссылок сгенерировано: ", amount,"\n")

if(answer == "y"):
  print("все ссылки сохранены в файл ", path_to_script, "\links.txt")

#to preduce closing of console on windows 
input()
