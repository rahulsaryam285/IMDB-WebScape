import requests
import json
from bs4 import BeautifulSoup
from Rahul_Task_1 import *
from Rahul_Task_4 import *
def get_movie_list_details(movies_list):
    movies=[]
    for data in movies_list:
        for url in data:
            movies.append(scrape_movie_details(data.get("Url")))
            break
    return movies
    
with open("Task_1.json","r") as data:
    movie_list=json.load(data)
data=get_movie_list_details(movie_list)
with open("Task_5.json","w") as obj:
    json.dump(data,obj,indent=4)


