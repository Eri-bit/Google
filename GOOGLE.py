#!/bin/python
# module
try:
   import os,sys,time,requests,bs4
   from bs4 import BeautifulSoup
   from time import sleep
   from os import system
except:
      system("pip install requests bs4")
# tampilan
def jalan():
    tampil = """
==============================================
{+} Author : Eri-bit
{+} Team   : Murid X Guru
{+} Github : Github.com/Eri-bit
=============================================="""
    system("clear")
    sleep(1)
    system("figlet Google")
    sleep(1)
    print(tampil)
    # isi data
    file = input("Masukan Pencarian: ")
    ulr = f"https://www.google.com/search?&q={file}"
    r = requests.get(ulr)
    cari = BeautifulSoup(r.text,"html.parser")
    a = cari.find("div",class_="BNeawe").text
    # hasil pencarian
    print("Hasil => ",a)

jalan()
