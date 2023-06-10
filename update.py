import json_utils
def update(sno,cname,contact,address):
    data=json_utils.Business("data/business.json")
    for company in data["Business"]:
        # print(sno,company["sno"])
        # print(type(sno),type(company["sno"]))
        if sno==str(company["sno"]):
            company["business_name"]=cname
            company["contact"]=contact
            company["add"]=address
    json_utils.write_json("data/business.json",data)
         