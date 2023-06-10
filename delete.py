import json_utils
def delete(sno):
    data=json_utils.Business("data/business.json")
    for company in data["Business"]:
        if str (company["sno"])==str(sno):
            data["Business"].remove(company)
    json_utils.write_json("data/business.json",data)
         
    
    