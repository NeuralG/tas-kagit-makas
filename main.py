
import random
from os import path
import os

def kazanan(x):
	if secimler[0] == x:
		print("KAZANDIN")
		kazanma()
	else:
		print("KAYBETTİN")
		kaybetme()

def oyun(x):

	global secimler

	secimim = x
	rakip = random.choice(["t","k","m"])

	print(rakip.upper())

	secimler = [secimim,rakip]

	if secimler[0] == secimler[1]:
		print("BERABERE")
		berabere()
	elif "t" not in secimler:
		print("Makas kağıdı keser")
		kazanan("m")
	elif "m" not in secimler:
		print("Kağıt taşı sarar")
		kazanan("k")
	elif "k" not in secimler:
		print("Taş makası ezer")
		kazanan("t")

def stats():
	file = open("stats.txt","r")

	nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw = file.readlines()

	print("""

		Oyuncu ismi = {}
		Altın miktarı = {}
		Üst üste kazanılan oyun = {}
		Kazanma oranı = {}
		Oynanan oyun = {}
		Kazanlılan oyun = {}
		Kaybeedilern oyun = {}
		Berabereler = {}



		""".format(nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw))

	file.close()

def kazanma():

	file = open("stats.txt","r")
	nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw = file.readlines()
	file.close()

	file = open("stats.txt","w")

	coin = int(coin) + 10
	winStreak = int(winStreak) + 1
	oyunSayisi = int(oyunSayisi) + 1
	win = int(win) + 1
	lose= int(lose)
	draw = int(draw)


	file.write("{}{}\n{}\n{}\n{}\n{}\n{}\n{}".format(nick,coin,winStreak,win/oyunSayisi*100,oyunSayisi,win,lose,draw))
	file.close()



def kaybetme():

	file = open("stats.txt","r")
	nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw = file.readlines()
	file.close()

	file = open("stats.txt","w")

	coin = int(coin) + 2
	winStreak = 0
	oyunSayisi = int(oyunSayisi) + 1
	win = int(win)
	lose= int(lose) + 1
	draw = int(draw)


	file.write("{}{}\n{}\n{}\n{}\n{}\n{}\n{}".format(nick,coin,winStreak,win/oyunSayisi*100,oyunSayisi,win,lose,draw))
	file.close()

def berabere():

	file = open("stats.txt","r")
	nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw = file.readlines()
	file.close()

	file = open("stats.txt","w")

	coin = int(coin) + 5
	winStreak = 0
	oyunSayisi = int(oyunSayisi) + 1
	win = int(win) 
	lose= int(lose)
	draw = int(draw) + 1

	file.write("{}{}\n{}\n{}\n{}\n{}\n{}\n{}".format(nick,coin,winStreak,win/oyunSayisi*100,oyunSayisi,win,lose,draw))
	file.close()


def isimDegistir():

	file = open("stats.txt","r")
	nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw = file.readlines()
	file.close()

	file = open("stats.txt","w")
	nick = input("Yeni isminizi giriniz: ")

	file.write("{}\n{}{}{}{}{}{}{}".format(nick,coin,winStreak,winRate,oyunSayisi,win,lose,draw))
	file.close()


def yeniOyuncumu():
	return not path.exists("stats.txt")

def yeniOyuncuOlustur():
	file = open("stats.txt","w")

	nick = input("Oyuncu ismini giriniz: ")

	file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(nick,15,0,0,0,0,0,0,0))


while True:

	if yeniOyuncumu():
		yeniOyuncuOlustur()

	print(""" 

		[0] = Oyun Oyna
		[1] = İstatistiklere bak
		[2] = İsmini değiştir
		[3] = Resetle
		[4] = Çık

		""")

	menu = input()

	if menu == "0":
		print("t,k,m?\n")
		secim = input() 

		oyun(secim)

	elif menu == "1":
		stats()

	elif menu == "2":
		isimDegistir()

	elif menu == "3":
		os.remove("stats.txt")
	else:
		break

