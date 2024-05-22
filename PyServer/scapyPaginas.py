urlT1="https://www.lostiempos.com/hemeroteca-noticias?f%5B0%5D=field_noticia_fecha%3A{A}&f%5B1%5D=field_noticia_fecha%3A2{AM}&f%5B2%5D=field_noticia_fecha%3A{AMD}"
urlT2="https://www.lostiempos.com/hemeroteca-fecha?fecha={D}%2F{M}%2F{A}&seccion=All"
urlbase="https://www.lostiempos.com"
urldeber="https://eldeber.com.bo/ultimas-noticias/{D}-{M}-{A}"
basedeber="https://eldeber.com.bo"
opiniourl="https://www.opinion.com.bo/archive/content/{A}/{M}/{D}"
baseOpinion="https://www.opinion.com.bo"
from progress.bar import Bar, ChargingBar
import datetime
from bs4 import BeautifulSoup as bs
import requests

def registercontend(fecha,text1,text2,pagina):
    import sqlite3
    con = sqlite3.connect("scrapinDatos.db")
    cur = con.cursor()
    cur.execute("create table if not exists data(title,description,fecha, pagina)")
    
    text1=text1.replace("'","")
    text2=text2.replace("'","")
    cur.execute("insert into data values ('{}','{}','{}','{}')".format(text1,text2,str(fecha),pagina))
    
    con.commit()

def scraping1(url,fecha):
    nr=0
    pag=requests.get(url.format(nro=nr))
    pag2=bs(pag.content,"html5lib")
    pagtext=pag2.text
    while not("Su búsqueda no tiene resultados" in pagtext ):
        
        pagtext=pag2.text
        ls=[]
        for x in  pag2.find_all('div',attrs={'class':"views-field",'class':'views-field-title'}) :
            try:
                if not(x.a['href'] in ls):
                    title=x.text
                    registercontend(text1=title,text2=title,fecha=fecha,pagina="Los Tiempos")
            except:
                pass   
        nr+=1 
        pag=requests.get(url.format(nro=nr))
        pag2=bs(pag.content,"html5lib")

def scraping2(url,fecha):
    pag=requests.get(url)
    pag2=bs(pag.content,"html5lib")
    ls=[]
    for x in  pag2.find_all('a',attrs={'class':"nota-link"}) :
        try:
            if not(x['href'] in ls):
                ls.append(x['href'])
                tex1=x.text
                registercontend(text1=tex1,text2=tex1,fecha=fecha,pagina="El Deber")
        except:
            break

def scraping3(url,fecha):
    nr=0
    pag=requests.get(url.format(nro=nr))
    pag2=bs(pag.content,"html5lib")
    pagtext=pag2.text
    for x in range(10):
        ls=[]
        for x in  pag2.find_all('div',attrs={'class':"views-field ",'class':"views-field-nothing"}) :
            try:
                if not(x.a['href'] in ls):
                    text1=x.a.text
                    text2=x.find('div',attrs={'class':'views-field-field-noticia-sumario'}).text
                    
                    registercontend(fecha=fecha,text1=text1,text2=text2,pagina="Los Tiempos")   
            except:
                pass
            
        try: 
            enc=pag2.find('li',{'class':'pager-next','class':'even','class':'last'})
            newUrl=urlbase+enc.a['href']
            pag=requests.get(newUrl)
        
            pag2=bs(pag.content,"html5lib")
            pagtext=pag2.text 
        except:
            break
from datetime import datetime, timedelta
def rangoFechas(inicio,fin):
    l1=inicio.split("/")
    l2=fin.split("/")
    inicio=datetime(int(l1[0]),int(l1[1]),int(l1[2]))
    fin=datetime(int(l2[0]),int(l2[1]),int(l2[2]))
    lista_fechas = [(inicio + timedelta(days=d)).strftime("%Y-%m-%d")
                    for d in range((fin - inicio).days + 1)] 
    return lista_fechas   

def extraer(fechaIncio,FechaFin):       
    for x in rangoFechas(fechaIncio,FechaFin):
                fechaLs=x.split('-')
                f1=fechaLs[0]
                f2=fechaLs[0]+"-"+fechaLs[1]
                nurl1=urlT1.format(A=f1,AM=f2,AMD=x)+"&page={nro}"
                nurl2=urlT2.format(A=fechaLs[0],M=fechaLs[1],D=fechaLs[2])
                nurl=basedeber.format(urldeber.format(D=fechaLs[2],M=fechaLs[1],A=fechaLs[0]))
                if(int(f1)<2017):
                    scraping1(nurl1,fecha=x)
                else:
                    scraping3(nurl2,fecha=x)
                
                scraping2(nurl,fecha=x)
                print("se obtuvo de:" +str(x))
# enero                
import sys
ls=sys.argv
print(ls)
extraer(ls[1],ls[2])