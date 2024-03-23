import requests
from bs4 import BeautifulSoup as bs
import re
import sys
import json
import os
from threading import Thread


spam = "oi"


def pega(passw):
	if passw == True:
		print("Url: ")
		ul = input("> ")
		print("")
		url = ul
		if url.startswith("https:"):
			urlcompleta = url
		else:
			sufixo = "/viewform"
			prefixo = "https://docs.google.com/forms/d/e/"
			urlcompleta = prefixo+url+sufixo
		with requests.session() as r:
			x = r.get(urlcompleta).text
			sopa = bs(x,"html.parser")
			form = sopa.find_all("div",class_="freebirdFormviewerViewNumberedItemContainer")
			file = open("entry.txt","w")
			file.write("{")
			for s in form:
				data = str(s)
				datap=data.split("=")
				datape = str(datap[4])####essencial
				if "jscontroller" in datape:
					img = str(s)
					imgsop = bs(img,"html.parser")
					imgv = imgsop.find_all("img")
					imgv = str(imgv)
					imgv = img.split("=")
					print("Foto: "+imgv[16]+'"')
				else:
					##############
					linha = datape.split(",")
					repostas = str(linha[5])
							##############
					numeros = re.findall(r'\d+',datape)
					enty = str(numeros[2])
							##############
					entry = "entry."
					if "[]" in repostas:
						repostas = "spam"
						ez = "'"+entry+enty+"'"+": "+"'"+repostas+"'"+","
						file.write(ez)
					else:
						repostas = repostas.split('"')[1]
						ez = "'"+entry+enty+"'"+": "+"'"+repostas+"'"+","
						file.write(ez)
			urlcompletac = urlcompleta.replace("viewform","formResponse")
			urlcompletac = urlcompletac.removeprefix("https://docs.google.com/forms/d/e/")
			urlcompletac = "https://docs.google.com/forms/u/0/d/e/" + urlcompletac
			file.write(urlcompletac)
			file.close()
	else:
		print("Incorrent password[X] ")
		sys.exit()

nu = 0
def comece(ed, siteurl):
	for x in range(100):
		with requests.session() as r:
			r.post(str(siteurl),data=ed)
			global nu
			nu += 1 
			print(f"Número de bots: {str(nu)}")
			os.system('cls')
def ir():
	texto=open("entry.txt","r")
	txt = texto.read()
	txt2 = str(txt)
	txtsep = txt2.split(",")
	#####
	quantida = len(txtsep)
	entryver = txtsep[0:quantida-1]
	siteurl = txtsep[-1]
	##### 
	et = str(entryver)
	ea = et.replace("spam",spam)
	es = ea.removeprefix("[")
	ed = es.removesuffix("]")###### enty true
	ed = ed+"}"
	ed = ed.removeprefix('"')
	ed = ed.replace('"', "")
	ed = ed.replace("'",'"')
	ed = json.loads(ed)
	#######
	try:
		with requests.session() as r:
			texto = r.post(str(siteurl),data=ed).text
			texto = bs(texto,"html.parser")
			texto = texto.find_all("a",class_="appsMaterialWizButtonNestedLink exportButtonNestedLink")
			texto = str(texto)
			texto = texto.split("=")
			site = texto[3]
			cont = texto[4].replace('"','')
			cont = cont.replace("rel","")
			print("Site: "+ texto[3]+"="+cont+'"')
			print("")
	except:
		print("")

	t1 = Thread(target=comece, args=(ed,siteurl)) 
	t1.start()
	t2 = Thread(target=comece, args=(ed,siteurl)) 
	t2.start()
	t3 = Thread(target=comece, args=(ed,siteurl)) 
	t3.start()
	t4 = Thread(target=comece, args=(ed,siteurl)) 
	t4.start()
	t5 = Thread(target=comece, args=(ed,siteurl)) 
	t5.start()
	t6 = Thread(target=comece, args=(ed,siteurl)) 
	t6.start()
	t7 = Thread(target=comece, args=(ed,siteurl)) 
	t7.start()
	t8 = Thread(target=comece, args=(ed,siteurl)) 
	t8.start()
	t9 = Thread(target=comece, args=(ed,siteurl)) 
	t9.start()
	t10 = Thread(target=comece, args=(ed,siteurl)) 
	t10.start()


if __name__ == "Main.py":
	pega(True)
	ir()
	
else:
	os.rename(__file__,"Main.py")
	pega(True)
	ir()