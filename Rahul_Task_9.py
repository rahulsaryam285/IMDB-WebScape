from Rahul_Task_1 import *  
import requests,json,random,time
from bs4 import BeautifulSoup
from Rahul_Task_4 import *
def scrape_movie_details(movie_url):
    random_sleep=random.randint(1,3)
    time.sleep(random_sleep)
    Url=requests.get(movie_url).text
    soup=BeautifulSoup(Url,"html.parser")
    title_div=soup.find("div",class_="title_wrapper").h1.get_text()
    name=""
    for x in title_div:
        if "(" not in x:
            name=(name+x).strip()
        else:
            break

    sub_div=soup.find("div",class_="subtext")
    runtime=sub_div.find("time").get_text().strip()
    runtime_hour=int(runtime[0])*60
    if "min" in sub_div:
        runtime_min=int(runtime[3:].strip("min"))
        movie_runtime=runtime_hour+runtime_min
    else:
        movie_runtime=runtime_hour
    
    gener=sub_div.find_all("a")
    gener.pop()
    movie_gener=[]
    for x in gener:
        movie_gener.append(x.get_text())
     
    summary=soup.find("div",class_="plot_summary")
    movie_bio=summary.find("div",class_="summary_text").get_text().strip()
 
    director=summary.find("div",class_="credit_summary_item")
    director_list=director.find_all("a")
    movie_director=[]
    for y in director_list:
        movie_director.append(y.get_text())

    extra_details=soup.find("div",attrs={"class":"article","id":"titleDetails"})
    list_of_divs=extra_details.find_all("div")
    
    for div in list_of_divs :
        tag_h4=div.find_all("h4")
        for text in tag_h4:
            if "Language:" in text:
                tag_anchor=div.find_all("a")
                movie_language=[]
                for language in tag_anchor:
                    movie_language.append(language.get_text())
            elif "Country:" in text:
                tag_anchor=div.find_all("a")
                for country in tag_anchor:
                    movie_contry=country.get_text()
                    # movie_contry.append(country.get_text())
    

    movie_poster_link=soup.find("div",class_="poster").a["href"]
    movie_poster="https://www.imdb.com" + movie_poster_link
    
    movie_detail_dic={"Name":"","Director":"","Country":"","Language":"","Poster_image_url":"","Bio_data":"","Runtime":"","Genre":""}
    movie_detail_dic["Name"]=name
    movie_detail_dic["Director"]=movie_director
    movie_detail_dic["Country"]=movie_contry
    movie_detail_dic["Language"]=movie_language
    movie_detail_dic["Poster_image_url"]=movie_poster
    movie_detail_dic["Bio_data"]=movie_bio
    movie_detail_dic["Runtime"]=movie_runtime
    movie_detail_dic["Genre"]=movie_gener
    return movie_detail_dic

# list_of_movie=movies250()
# new_list=[]
# for x in range(len(list_of_movie)):
#     new_list.append(scrape_movie_details(list_of_movie[x]["Url"]))
# with open("Task_4.json","w") as obj:
#     json.dump(new_list,obj,indent=4)


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
with open("Task_9.json","w") as obj:
    json.dump(data,obj,indent=4)