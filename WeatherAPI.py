from bs4 import BeautifulSoup as bs
import urllib2
import re
LAT=26.17
LON=85.89
def get5days():
    # url="http://wttr.in/"+str(LAT)+","+str(LON)+"?q2"
    url="http://www.accuweather.com/en/in/darbhanga/3241077/migraine-daily-forecast/3241077"
    data=urllib2.urlopen(url)
    data=data.read()
    soup=bs(data,'html.parser')
    # print data
    forecast=str(soup.findAll('div',class_="panel-list lifestyle-panel five-panel")[0]).strip()
    soup=bs(forecast,'html.parser')
    # for i in soup.findAll('ul'):
    #     print "----------------------------------------------------------------------------------"
    #     # print i
    #     print "----------------------------------------------------------------------------------"
    arrMax,arrMin="",""
    for i in soup.findAll('span',class_="large-temp"):
        arrMax+=str(i)
    for i in soup.findAll('span',class_="small-temp"):
        arrMin+=str(i)
    # print arr
    patternMax=re.compile('<span class="large-temp">([0-9]+)<span>')
    patternMin=re.compile('<span class="small-temp">/([0-9]+)')
    maxx=re.findall(patternMax,arrMax)
    minn=re.findall(patternMin,arrMin)
    ans=[]
    for a,b in zip(maxx,minn):
        ans.append( (a,b)  )
    return ans
