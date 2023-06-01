import json_utlis
def update(sno,cname,contact,address):
    data=json_utlis.Business("data/business.json")
    for company in data["Business"]:
        # print(sno,company["sno"])
        # print(type(sno),type(company["sno"]))
        if sno==str(company["sno"]):
            company["business_name"]=cname
            company["contact"]=contact
            company["add"]=address
    json_utlis.write_json("data/business.json",data)
         