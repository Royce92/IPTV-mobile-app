import json
import requests
from bs4 import BeautifulSoup

def getlinks():
    file = open("123m3u8.txt", "w") # save request file

    #https://raw.githubusercontent.com/podgod/podgod/master/cCloud_TV_Guide/XML/combined.ini
    r = requests.get('https://raw.githubusercontent.com/singhlol/singhlol/master/lists/kodi.txt', stream = True)
    plain_text = r.text
    soup = BeautifulSoup(r.text, "html.parser") 
    for links in soup:
        file.write(str(links))
    file.close()
getlinks()    

def final():
    fullm3u8 = open("fullm3u8.json", "w")
    dic = {"channels":[],"OnDemandMovies":[],"Adult":[],"OnDemandShows":[],"Special Events":[],"RandomAirTime 24/7":[],
           "Public-Family":[],"Public-Movie Channels":[],"Public-Sports":[],"Documentary":[],"Movie Channels":[],"Entertainment":[],"Public-Documentary":[],
"Family":[],"Comedy":[],"News":[],"Music":[],"Lifestyle":[],"Sports":[],"Radio":[],"DIY":[]}

    tempdic = {}
    templ = []
    with open("123m3u8.txt") as f:
        t = ["a"]

        temp = None
        e = "temp"
        for name in f.readlines():
            name = name.replace(") ", "").replace("https://archive.org/download/cCloud_20151126/cCloud.mp4","").replace("cCloudTV.ORG", "").replace("|User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20WOW64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F47.0.2526.106%20Safari%2F537.36","")
            if name.startswith("http") != True and "cCloud" not in name:
                temp = name
            else:
                e = temp+name
            if e not in t:
                t.append(e)
                #print(e)
                name = (e[e.find("name")+int(6):e.find("tvg-language=")-int(2)])
                url = (e[e.find(")")+int(1):])
                #print(e[e.find("http"):] and e.find("m3u8") == 0)
                #if dic[channels][channel]
                dic["channels"].append({"channel":name.strip(),"url":url.strip()})

                
                category = (e[e.find("group-title")+int(13):e.find('",')])
                if category in e:
                    t.append(e)
                    print(category)
                    #print(e)
                    name = (e[e.find("name")+int(6):e.find("tvg-language=")-int(2)])
                    url = (e[e.find(")")+int(1):])
                    #print(e[e.find("http"):] and e.find("m3u8") == 0)
                    #if dic[channels][channel]
                    try:
                        dic[category].append({"channel":name.strip(),"url":url.strip()})
                    except KeyError:
                        print("no good", category)

        fullm3u8.write(json.dumps(dic))
           # print(dic)

    fullm3u8.close()
final()
