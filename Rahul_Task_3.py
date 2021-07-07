
import json
from Rahul_Task_2 import *
data=fun_list_1
def group_by_decade(movies):
    new_dict={}
    new=[]
    for data in movies:
        remain=data%10
        sub=data-remain
        if sub not in new:
            new.append(sub)
        new.sort()
    for year in new:
        new_dict[year]=[]
    for data in new_dict:
        Add=data+9
        for movie in movies:
            if movie <= Add and movie >= data:
                for name in movies[movie]:
                    new_dict[data].append(name)
    return  new_dict

fun_list_2=group_by_decade(data)
with open("Task_3.json","w") as obj:
    json.dump(fun_list_2,obj,indent=4)
