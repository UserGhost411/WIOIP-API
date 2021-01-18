from lib.static import urlAPI,errorMessage,headers,urlIP
import requests
import json
from flask import redirect,request as req
def getRootData():
  return redirect("https://github.com/UserGhost411/WIOIP/")
def getWeather(h="all",region=""):
    ip_address = req.headers['X-Forwarded-For']#.remote_addr
    page = requests.get( urlIP+ip_address, headers=headers)
    if(region==""):
        if page.status_code == 200:
            va = json.loads(page.text)
            print(va)
            location = va['city']#Kenjeran, Surabaya City, East Java
            cord = ""
            if(" " in location): cord = str(va['lat'])+","+str(va['lon'])
            dat = {"status":1,"city": va['city'],"region": va['regionName'],"country": va['country']}
            if(h=="c" or h=="all"):dat['current'] = json.loads(requests.get( urlAPI+"current?location="+cord+"&format=json&city="+location, headers=headers).text)
            if(h=="f" or h=="all"):dat['forecast']  = json.loads(requests.get( urlAPI+"forecast?location="+cord+"&format=json&city="+location, headers=headers).text)
            return dat
        else:
            return errorMessage
    else:
        loc = json.load(open("loc.json",))
        hasil = LinearSearch(loc,region.lower())
        if(hasil):
            location = hasil[0]['city']
            cord = str(hasil[0]['lat'])+","+str(hasil[0]['long'])
            dat = {"status":1,"city": hasil[0]['city'],"region": hasil[0]['city'],"country": hasil[0]['city']}
            if(h=="c" or h=="all"):dat['current'] = json.loads(requests.get( urlAPI+"current?location="+cord+"&format=json&city="+location, headers=headers).text)
            if(h=="f" or h=="all"):dat['forecast']  = json.loads(requests.get( urlAPI+"forecast?location="+cord+"&format=json&city="+location, headers=headers).text)
            return dat
        else:
            return errorMessage
def region(nama):
    loc = json.load(open("loc.json",))
    hasil = LinearSearch(loc,nama.lower())
    return {"result":hasil,"count":len(hasil)}
def LinearSearch(data, element):
    tmp = []
    for i in range(len(data)):
        if element in data[i]['city']:
            tmp.append(data[i])
    return tmp