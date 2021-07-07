import json
import requests
from bs4 import BeautifulSoup
def scrape_movie_cast(movie_cast_url):
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
    # json_data=new_list[:]
    # print(json_data)
    return  new_list

a="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
# scrape_movie_cast(a)
with open("Task_12.json","w") as obj:
    json.dump(scrape_movie_cast(a),obj,indent=4)

# a=[1,2,3]
# b=[5,6,7]
# a=b[:]
# print(a)
    
    