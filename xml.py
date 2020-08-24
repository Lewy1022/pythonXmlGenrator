# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:43:46 2020

@author: Woland
"""

import cx_Oracle
#import xmlify
import datetime
from lxml import etree
from random import randrange
import sys

con = cx_Oracle.connect('hr','hr','orcl4')
    
cur = con.cursor()
cur.execute('select * from Klient')
wartosc = cur.fetchall()
lista =wartosc[2]

test = str(lista[0])




def export_klient(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Klient')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-klient')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'klient')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'imie')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'nazwisko')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'karnet')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'trener')
        child.text = str(test[4])
        child = etree.SubElement(prod, 'id_kontakt')
        child.text = str(test[5])
        child = etree.SubElement(prod, 'id_adres')
        child.text = str(test[6])
        child = etree.SubElement(prod, 'waznosc')
        child.text = str(test[7])
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()

def import_klient(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    klienci = importedXml.findall('klient')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Klient')
    wartosc = cur.fetchone()
    ostatnieIdKlienta = int(wartosc[0])
    i=0
    for c in klienci:
        querry ="Insert INTO Klient VALUES ("+str(ostatnieIdKlienta+3)+",'"+c.find('imie').text+"','"+c.find('nazwisko').text+"',"+c.find('karnet').text+","+c.find('trener').text+","+c.find('id_kontakt').text+","+c.find('id_adres').text+",TO_DATE('2020/"+str(randrange(1,12))+"/"+str(randrange(1,30))+" 21:02:44', 'yyyy/mm/dd hh24:mi:ss'))"
        cur.execute(querry)
        ostatnieIdKlienta=ostatnieIdKlienta+1
    
    cur.execute('commit')
    
    
def export_trener(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()
    cur.execute('select * from Trener')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-trener')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'trener')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'imie')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'nazwisko')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'id_kontakt')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'id_adres')
        child.text = str(test[4])
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
def import_trener(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('trener')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Trener')
    wartosc = cur.fetchone()
    ostatnieIdTrenera = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Trener VALUES ("+str(ostatnieIdTrenera+1)+",'"+c.find('imie').text+"','"+c.find('nazwisko').text+"',"+c.find('id_kontakt').text+","+c.find('id_adres').text+")"

        cur.execute(querry)
        ostatnieIdTrenera=ostatnieIdTrenera+1
    
    cur.execute('commit')
    
def export_kontakt(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Kontakty')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-kontakt')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'kontakt')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'nrTel')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'nrTel2')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'email')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'www')
        child.text = str(test[4])
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
  
def import_kontakty(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('kontakt')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Kontakty')
    wartosc = cur.fetchone()
    ostatnieIdKontaktu = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Kontakty VALUES ("+str(ostatnieIdKontaktu+1)+",'"+c.find('nrTel').text+"',NULL,'"+c.find('email').text+"',NULL)"

        cur.execute(querry)
        ostatnieIdKontaktu=ostatnieIdKontaktu+1
    
    cur.execute('commit')
    
    
def export_adres(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Adresy')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-adres')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'adres')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'miasto')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'miejscowos')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'wojewodztwo')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'powiat')
        child.text = str(test[4])
        child = etree.SubElement(prod, 'kodPocztowy')
        child.text = str(test[5])
        child = etree.SubElement(prod, 'ulica')
        child.text = str(test[6])
        child = etree.SubElement(prod, 'nrDomu')
        child.text = str(test[7])
        child = etree.SubElement(prod, 'nrMieszkania')
        child.text = str(test[8])
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
def import_adres(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('adres')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Adresy')
    wartosc = cur.fetchone()
    ostatnieIdAdresu = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Adresy VALUES ("+str(ostatnieIdAdresu+1)+",'"+c.find('miasto').text+"',NULL,'"+c.find('wojewodztwo').text+"','"+c.find('powiat').text+"','"+c.find('kodPocztowy').text+"','"+c.find('ulica').text+"','"+c.find('nrDomu').text+"',NULL)"

        cur.execute(querry)
        ostatnieIdAdresu=ostatnieIdAdresu+1
    
    cur.execute('commit')
    
    
def export_cennik(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Cennik')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-cennik')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'cennik')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'karnet')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'cena')
        child.text = str(test[2])
       
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
def import_cennik(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('cennik')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Cennik')
    wartosc = cur.fetchone()
    ostatnieIdCennika = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Cennik VALUES ("+str(ostatnieIdCennika+1)+",'"+c.find('karnet').text+"','"+c.find('cena').text+"')"

        cur.execute(querry)
        ostatnieIdCennika=ostatnieIdCennika+1
    
    cur.execute('commit')
    
    
def export_cwiczenie(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()
    cur.execute('select * from Cwiczenia')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-cwiczenia')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'cwiczenie')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'nazwa')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'partia')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'typ')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'sprzet')
        child.text = str(test[4])
        child = etree.SubElement(prod, 'trudnosc')
        child.text = str(test[5])
       
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
    
def import_cwiczenia(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('cwiczenie')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Cwiczenia')
    wartosc = cur.fetchone()
    ostatnieIdCwiczenia = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Cwiczenia VALUES ("+str(ostatnieIdCwiczenia+1)+",'"+c.find('nazwa').text+"','"+c.find('partia').text+"','"+c.find('typ').text+"','"+c.find('sprzet').text+"','"+c.find('trudnosc').text+"')"
        cur.execute(querry)
        ostatnieIdCwiczenia=ostatnieIdCwiczenia+1
    
    cur.execute('commit')
    
    
def export_grafik(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()
    cur.execute('select * from Grafik')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-grafik')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'grafik')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'idTrenera')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'godzRozpoczecia')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'godzZakonczenia')
        child.text = str(test[3])

        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
    
def import_grafik(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('grafik')
    
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()


    cur.execute('select count(*) from Grafik')
    wartosc = cur.fetchone()
    ostatnieIdGrafiku = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Grafik VALUES ("+str(ostatnieIdGrafiku+1)+","+c.find('idTrenera').text+","+c.find('godzRozpoczecia').text+","+c.find('godzZakonczenia').text+")"

        cur.execute(querry)
        ostatnieIdGrafiku=ostatnieIdGrafiku+1
    
    cur.execute('commit')
  
    
def export_plan(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()
    cur.execute('select * from Plan_treningu')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-plan')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'plan')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'idKlienta')
        child.text = str(test[1])
       
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
    
def import_plan(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('plan')
    
    con = cx_Oracle.connect('hr','hr','orcl4')   
    cur = con.cursor()


    cur.execute('select count(*) from Plan_treningu')
    wartosc = cur.fetchone()
    ostatnieIdPlanu = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Plan_treningu VALUES ("+str(ostatnieIdPlanu+1)+","+c.find('idKlienta').text+")"
 
        cur.execute(querry)
        ostatnieIdPlanu=ostatnieIdPlanu+1
    
    cur.execute('commit')
    
def export_planCwiczen(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Plan_cwiczen')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-planCwiczen')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'planCwiczen')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'dzien')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'iloscSeri')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'cwiczenie')
        child.text = str(test[3])
        child = etree.SubElement(prod, 'idPlanuTreningu')
        child.text = str(test[4])
        child = etree.SubElement(prod, 'iloscPowtorzen')
        child.text = str(test[5])
       
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
  
    
def import_planCwiczen(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('planCwiczen')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Plan_cwiczen')
    wartosc = cur.fetchone()
    ostatnieIdPlanCwiczen = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Plan_cwiczen VALUES ("+str(ostatnieIdPlanCwiczen+1)+",'"+c.find('dzien').text+"',"+c.find('iloscSeri').text+","+c.find('cwiczenie').text+","+c.find('idPlanuTreningu').text+","+c.find('iloscPowtorzen').text+")"
        cur.execute(querry)
        ostatnieIdPlanCwiczen=ostatnieIdPlanCwiczen+1
    
    cur.execute('commit')
    
    
def export_rejestrWejsc(xmlFileName):
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()
    cur.execute('select * from Rejestr_wejsc_wyjsc')
    wartosc = cur.fetchall()

    xmlFile = open(xmlFileName, 'w',encoding='utf-8')

    root = etree.Element('Tabela-rejestr')
    for x in range(0,len(wartosc)):
        test = wartosc[x]
        prod = etree.SubElement(root,'rejestr')
        child = etree.SubElement(prod, 'id')
        child.text = str(test[0])
        child = etree.SubElement(prod, 'id_osoby')
        child.text = str(test[1])
        child = etree.SubElement(prod, 'dataWejscia')
        child.text = str(test[2])
        child = etree.SubElement(prod, 'dataWyjscia')
        child.text = str(test[3])

       
        
    
    str2 = etree.tostring(root, pretty_print=True, encoding ='unicode')
    xmlFile.write(str2)
    xmlFile.close()
    
def import_rejestrWejsc(xmlFileName):
    importedXml = etree.parse(xmlFileName)
    trenerzy = importedXml.findall('rejestr')
    
    con = cx_Oracle.connect('hr','hr','orcl4')    
    cur = con.cursor()


    cur.execute('select count(*) from Rejestr_wejsc_wyjsc')
    wartosc = cur.fetchone()
    ostatnieIdRejestr_wejsc_wyjsc = int(wartosc[0])
    i=0
    for c in trenerzy:
        querry ="Insert INTO Rejestr_wejsc_wyjsc VALUES ("+str(ostatnieIdRejestr_wejsc_wyjsc+1)+","+c.find('id_osoby').text+",TO_TIMESTAMP( '2019-03-02 14:53:20','YYYY-MM-DD HH24:MI:SS'),TO_TIMESTAMP( '2019-03-02 16:33:20','YYYY-MM-DD HH24:MI:SS'))"
 
        cur.execute(querry)
        ostatnieIdRejestr_wejsc_wyjsc=ostatnieIdRejestr_wejsc_wyjsc+1
    
    cur.execute('commit')
    
  
    
    
if len(sys.argv)==4:
    if sys.argv[1] =="eksport":
        if sys.argv[2]=='klient' or sys.argv[2]=='Klient':
            export_klient(sys.argv[3])
        elif sys.argv[2]=='Trener' or sys.argv[2]=='trener':
            export_trener(sys.argv[3])
        elif sys.argv[2]=='Kontakty' or sys.argv[2]=='kontakty':
            export_kontakt(sys.argv[3])
        elif sys.argv[2]=='cennik' or sys.argv[2]=='Cennik':
            export_cennik(sys.argv[3])
        elif sys.argv[2]=='Cwiczenia' or sys.argv[2]=='cwiczenia':
            export_cwiczenie(sys.argv[3])
        elif sys.argv[2]=='Grafik' or sys.argv[2]=='grafik':
            export_grafik(sys.argv[3])
        elif sys.argv[2]=='plan_treningu' or sys.argv[2]=='Plan_treningu':
            export_plan(sys.argv[3])
        elif sys.argv[2]=='Plan_cwiczen' or sys.argv[2]=='plan_cwiczen':
            export_planCwiczen(sys.argv[3])
        elif sys.argv[2]=='Rejestr_wejsc_wyjsc' or sys.argv[2]=='rejestr_wejsc_wyjsc':
            export_rejestrWejsc(sys.argv[3])
        elif sys.argv[2]=='Adresy' or sys.argv[2]=='adresy':
            export_adres(sys.argv[3])
    
    elif sys.argv[1] =="import":
        if sys.argv[2]=='klient' or sys.argv[2]=='Klient':
            import_klient(sys.argv[3])
        elif sys.argv[2]=='Trener' or sys.argv[2]=='trener':
            import_trener(sys.argv[3])
        elif sys.argv[2]=='Kontakty' or sys.argv[2]=='kontakty':
            import_kontakty(sys.argv[3])
        elif sys.argv[2]=='cennik' or sys.argv[2]=='Cennik':
            import_cennik(sys.argv[3])
        elif sys.argv[2]=='Cwiczenia' or sys.argv[2]=='cwiczenia':
            import_cwiczenia(sys.argv[3])
        elif sys.argv[2]=='Grafik' or sys.argv[2]=='grafik':
            import_grafik(sys.argv[3])
        elif sys.argv[2]=='plan_treningu' or sys.argv[2]=='Plan_treningu':
            import_plan(sys.argv[3])
        elif sys.argv[2]=='Plan_cwiczen' or sys.argv[2]=='plan_cwiczen':
            import_planCwiczen(sys.argv[3])
        elif sys.argv[2]=='Rejestr_wejsc_wyjsc' or sys.argv[2]=='rejestr_wejsc_wyjsc':
            import_rejestrWejsc(sys.argv[3])
        elif sys.argv[2]=='Adresy' or sys.argv[2]=='adresy':
            import_adres(sys.argv[3])
        
        
        
else:
    print('bledna liczba argumentow')
