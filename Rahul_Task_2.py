import json
from Rahul_Task_1 import movies250
def group_by_year(movies):        
    years=[]
    for data in movies:
        year=data["Year"]
        if year not in years:
            years.append(year)
    new_dict={}
    for data in years:
        new_dict[data]=[]
    for movie in movies:
        value=movie["Year"]
        for data in new_dict:
            if data==value:
                new_dict[data].append(movie)
    return new_dict

fun_list_1=group_by_year(movies250())
with open("Task_2.json","w") as obj:
    json.dump(fun_list_1,obj,indent=4)
