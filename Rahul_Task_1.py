import requests
from bs4 import BeautifulSoup 
import json
url=requests.get(" https://www.imdb.com/india/top-rated-indian-movies/").text
def movies250():
    soup=BeautifulSoup(url,"html.parser")
    names=soup.find_all(class_="titleColumn")
    years=soup.find_all(class_="secondaryInfo")
    rating=soup.find_all(class_="ratingColumn imdbRating")
    list1=[]
    list2=[]
    list3=[]
    for name in names:
        list1.append(name.find("a").text)
        list2.append("https://www.imdb.com"+name.find("a").get("href"))
        list3.append(int(name.text.strip().split(".")[0]))
    list4=[]
    for year in years:
        list4.append(int(year.text[1:5]))
    list5=[]
    for rat in rating:
        list5.append(float(rat.text.strip()))
    new_list=[]
    # dict={}
    for i,j,k,u,m in zip(list1,list4,list3,list5,list2):
        dict={}
        dict["Name"]=i
        dict["Year"]=j
        dict["Postion"]=k
        dict["Rating"]=u
        dict["Url"]=m
        new_list.append(dict)
        # new_list.append(dict.copy())
    return new_list
fun_list=movies250()
with open("Task_1.json","w") as obj:
    json.dump(fun_list,obj,indent=4)


