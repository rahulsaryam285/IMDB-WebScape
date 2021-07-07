import json
import requests
from bs4 import BeautifulSoup
def scrape_movie_cast(movie_cast_url,dict):
    raw=requests.get(movie_cast_url).text
    soup=BeautifulSoup(raw,"html.parser")
    json_data=raw
    data=soup.find("table",class_="cast_list")
    actor_data=data.find_all("td",class_="")
    new_list=[]
    for x in actor_data:
        new_dict={}
        id=x.find("a")
        imdb_id=id.get("href")[6:15]
        Hero_name=x.get_text().strip()
        new_dict["IMDB_id"]=imdb_id
        new_dict["Name"]=Hero_name
        new_list.append(new_dict)
    dict["Cast"]=new_list
    return  dict
with open("Task_1.json","r") as read:
    data=json.load(read)

with open("Task_4.json","r") as read1:
    data1=json.load(read1)
old_list=[]
a=len(data)
for dict in range(a):
    for key in data[dict]:
        old_list.append(scrape_movie_cast(data[dict].get("Url")+"fullcredits?ref_=tt_cl_sm#cast",data1[dict]))
        break

with open("Task_13.json","w") as obj:
    json.dump(old_list,obj,indent=4)

    
