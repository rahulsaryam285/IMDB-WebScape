import json
def analyse_movies_gener(movies_list):
    movies={}
    for dict in movies_list:
        for key in dict:
            value=dict.get("Genre")
            break
        for x in value:
            if x in movies:
                movies[x]=movies[x]+1
            else:
                movies[x]=1
    return  movies

with open("Task_5.json","r") as obj:
    Details=json.load(obj)
data=analyse_movies_gener(Details)
with open("Task_11.json","w") as obj:
    json.dump(data,obj,indent=4)