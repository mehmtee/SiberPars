import requests
from bs4 import BeautifulSoup
import sys
import random
print("""
  ____                
 |  _ \ __ _ _ __ ___ 
 | |_) / _` | '__/ __|*
 |  __/ (_| | |  \__ \ 
 |_|   \__,_|_|  |___/



Version : 0.1

Dikkat! Bu program Siber Pars projesinin ilk sürümüne ait
bir modüldür.

Projenin gelişmesine yardımcı olmak
açısından wdPdd klasörünü yazılımcı ile 
paylaşınız.


 Coded by mehmtee

                      



	""")


def bing_Src(sorgu,s):
	#sorgu = aramasayisi
	#s =dork
	print(("Girilen arama sınırı : {} ").format(sorgu))
	print(("Girilen dork : {}     ").format(s))
	


	def yapı(sorgu,s):
		global siteler

		siteler =[]

		tew = ['x','y','z','g','he']
		x = random.randint(0,255)
		y = random.randint(0,757512)
		
		
		f = requests.Session()
		f.verify = '/path/to/certfile'

		
		hed = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}


		url = ("""
https://www.bing.com/search?q={}&qs=n&sp=-1&pq={}&sc=8-3&sk=&cvid=692DE830120B4DCBAB98329128984556&first={}&FORM=PERE
		""".format(sorgu,sorgu,s))
		r = requests.post(url,headers=hed)

		kod = BeautifulSoup(r.content,'lxml')
		
		
		
		#https://www.google.com.tr/
		parsel = kod.find('cite').text


		print(("""
[+] {}

""").format(parsel))
		parsel = str(parsel)
		
		file_path ="url.txt"
		with open(file_path,'a') as file:
			file.write(parsel+"\n")
		

		










	qs =1
	while qs<sorgu:
		yapı(s,qs)
		qs = qs+1





	
		


arama_sayisi = sys.argv[1]
dork = sys.argv[2]
arama_sayisi = arama_sayisi[2:len(arama_sayisi)]
dork = dork[2:len(dork)]
arama_sayisi = int(arama_sayisi)
bing_Src(arama_sayisi,dork)
