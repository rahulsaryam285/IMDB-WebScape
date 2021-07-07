import json
def analyse_language_and_directors(movies_list):
    dict={}
    for dict1 in movies_list:
        for value in dict1["Director"]:
            dict[value]={}
        for x in range(len(movies_list)):
            for director in dict:
                if director in movies_list[x]["Director"]:
                    for language in movies_list[x]["Language"]:
                        dict[director][language]=0
        for x in range(len(movies_list)):
            for director in dict:
                if director in movies_list[x]["Director"]:
                    for language in movies_list[x]["Language"]:
                        dict[director][language]+=1           
    return dict
    
    ###incomplete
    # new_dict={}
    # for dict1 in movies_list:
    #     for key in dict1:
    #         value_director=dict1.get("Director")
    #         value_language=dict1.get("Language")
    #         print(value_director)
    #         print(value_language)
        #     if value_director not in dict:
        #         dict[value_director]={}
        # print(dict)
    #     for y in value_language:
    #         if y in new_dict:
    #             new_dict[y]=new_dict[y]+1
    #         else:
    #             new_dict[y]=1
    # print(dict)  
        
with open("Task_9.json","r") as obj:
    data=json.load(obj)
analyse_language_and_directors(data)
store_dict=analyse_language_and_directors(data)
with open("Task_10.json","w") as dict:
    json.dump(store_dict,dict,indent=4)
