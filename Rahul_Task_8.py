import json
with open("Task_5.json","r") as data:
    movie_list=json.load(data)
for dict1 in movie_list[:5]:
    for key in dict1:
        movie_num=dict1.get("Poster_image_url")[27:36]
        format="{}.json".format(movie_num)
        with open(format,"w") as obj:
            json.dump(dict1,obj,indent=4)
        break