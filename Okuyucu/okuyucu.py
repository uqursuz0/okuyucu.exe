import time
import os
import keyboard
metin=open("text.txt","r") 
metin= metin.read()

listmetin=metin.split("|")
uzunluk=0
for kelime in listmetin:
    if len(kelime)>uzunluk:
        uzunluk=len(kelime)
input("a"*uzunluk)
for kelime in listmetin:
    os.system("cls")
    print(kelime.center(uzunluk))
    süre=len(kelime)
    time.sleep(süre/15)
    if keyboard.is_pressed("s"):
        keyboard.wait("d")

    # recorded = keyboard.record(until="right arrow")
    