import json
import os

def doDump(fileName):
    file = open(fileName,"r")
    data = json.load(file)
    
    array = data["questions"]
    
    i = 0
    j=0
    newObj = []
    for item in array:
        if(len(item["Question"]) <= 120):
           
            if(len(item["optionA"]+item["optionA"]+item["optionA"]+item["optionA"])<=100):
                 #print("yes")
                 newObj.append(item)
                 i+=1
            else:
                #print("no")
                j+=1
        else:
            #print("no")
            j+=1
        
    #print(i,j)
    
    dictionary = {
        "questions":newObj
    }
    
    with open(f"{fileName}", "w") as outfile:
        json.dump(dictionary, outfile)

files = os.listdir("raw/science")

for file in files:
    # print("raw/geography/"+file)
    doDump("raw/science/"+file)